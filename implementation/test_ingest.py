import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

# Importing ingest normally loads credentials and constructs an API client.
with patch("dotenv.load_dotenv"), patch("openai.OpenAI"):
    import ingest


class CreateEmbeddingsTests(unittest.TestCase):
    def test_batches_preserve_chunk_order_and_metadata(self):
        for count, expected_sizes in (
            (1, [1]),
            (128, [128]),
            (129, [128, 1]),
            (2050, [128] * 16 + [2]),
        ):
            with self.subTest(count=count):
                self.check_batches(count, expected_sizes)

    def check_batches(self, count, expected_sizes):
        chunks = [
            ingest.Result(page_content=f"text {i}", metadata={"source": f"source {i}"})
            for i in range(count)
        ]
        batches = []

        def create_embeddings(*, model, input):
            self.assertEqual(model, ingest.embedding_model)
            self.assertLessEqual(len(input), 2048)
            batches.append(input)
            return SimpleNamespace(
                data=[
                    SimpleNamespace(embedding=[float(text.split()[-1])])
                    for text in input
                ]
            )

        client = MagicMock()
        collection = client.get_or_create_collection.return_value
        with (
            patch.object(ingest, "PersistentClient", return_value=client),
            patch.object(
                ingest.openai.embeddings, "create", side_effect=create_embeddings
            ),
        ):
            ingest.create_embeddings(chunks)

        self.assertEqual([len(batch) for batch in batches], expected_sizes)
        kwargs = collection.add.call_args.kwargs
        self.assertEqual(kwargs["ids"], [str(i) for i in range(count)])
        self.assertEqual(kwargs["documents"], [chunk.page_content for chunk in chunks])
        self.assertEqual(kwargs["metadatas"], [chunk.metadata for chunk in chunks])
        self.assertEqual(kwargs["embeddings"], [[float(i)] for i in range(count)])


if __name__ == "__main__":
    unittest.main()
