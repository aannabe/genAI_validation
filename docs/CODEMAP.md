# Code map

Agents: read this file first, then search for what you need instead of opening many files.
The **Overview** is maintained by hand (keep it short). The **Generated index** is rewritten by
`uv run --no-project scripts/codemap.py`; never edit it by hand.

## Overview

| Path | Purpose |
|---|---|
| `AGENTS.md` | Universal agent rules (single source of truth for every AI provider) |
| `.agents/skills/<name>/SKILL.md` | On-demand Python and task skills |
| `python/` | Python source files and pytest tests |
| `pyproject.toml`, `uv.lock` | Python project, Ruff, and pytest configuration |
| `scripts/codemap.py` | Python utility that regenerates this map |
| `docs/` | Documentation, including this map |

Build and test:
- Python: `uv run ruff check .`, `uv run ruff format --check .`, `uv run pytest`

Add application code under `python/` and tests under `python/tests/`.

## Generated index

<!-- BEGIN GENERATED (scripts/codemap.py) -->
### Languages

| Language | Files | Lines |
|---|---:|---:|
| Markdown | 109 | 7192 |
| Other | 16 | 2381 |
| Python | 9 | 1277 |
| JSON | 3 | 91 |
| TOML | 1 | 53 |

### Files (line counts)

```
./
  .editorconfig (15)
  .gitattributes (5)
  .gitignore (19)
  .python-version (1)
  AGENTS.md (61)
  CLAUDE.md (6)
  GEMINI.md (4)
  LICENSE (21)
  README.md (145)
  app.py (61)
  evaluator.py (291)
  pyproject.toml (53)
.agents/skills/code-review/
  SKILL.md (21)
.agents/skills/debugging/
  SKILL.md (20)
.agents/skills/docs-and-codemap/
  SKILL.md (18)
.agents/skills/git-workflow/
  SKILL.md (17)
.agents/skills/python/
  SKILL.md (34)
.agents/skills/refactoring/
  SKILL.md (18)
.agents/skills/security/
  SKILL.md (22)
.agents/skills/testing/
  SKILL.md (20)
.claude/
  settings.json (35)
.github/
  copilot-instructions.md (11)
.vscode/
  settings.json (31)
docs/
  CODEMAP.md (198)
evaluation/
  eval.py (244)
  stress.jsonl (54)
  stress_kb_manifest.json (25)
  test.py (58)
  tests.jsonl (150)
implementation/
  answer.py (156)
  ingest.py (151)
initial_eval_results/
  eval_Answer.log (1058)
  eval_GUI.png
  eval_RAG.log (1058)
initial_eval_results/preprocessed_db/
  chroma.sqlite3
initial_eval_results/preprocessed_db/abb854d6-52d0-452c-8daf-687e35a086a1/
  data_level0.bin
  header.bin
  index_metadata.pickle
  length.bin
  link_lists.bin
knowledge-base/company/
  Northwind Data Services Capability Statement.md (26)
  Recruiting Log Claims Data Analyst.md (38)
  about.md (16)
  careers.md (139)
  culture.md (37)
  overview.md (51)
knowledge-base/contracts/
  Contract with Advantage Medical Coverage for Healthllm.md (93)
  Contract with Apex Reinsurance for Rellm - AI-Powered Enterprise Reinsurance Solution.md (53)
  Contract with Atlantic Risk Solutions for Bizllm.md (101)
  Contract with Belvedere Insurance for Markellm.md (43)
  Contract with BrightWay Solutions for Markellm.md (63)
  Contract with Cascade Mutual for Healthllm.md (60)
  Contract with ConnectInsure Agency for Markellm.md (141)
  Contract with Continental Commercial Group for Bizllm.md (131)
  Contract with DriveSmart Insurance for Carllm.md (198)
  Contract with EverGuard Insurance for Rellm - AI-Powered Enterprise Reinsurance Solution.md (58)
  Contract with Evergreen Life Insurance for Lifellm.md (137)
  Contract with FastTrack Insurance Services for Claimllm.md (73)
  Contract with Fortress Business Underwriters for Bizllm.md (87)
  Contract with GlobalRe Partners for Rellm.md (292)
  Contract with GreenField Holdings for Markellm.md (34)
  Contract with GreenValley Insurance for Homellm.md (77)
  Contract with Greenstone Insurance for Homellm.md (73)
  Contract with Guardian Life Partners for Lifellm.md (121)
  Contract with Harmony Health Plans for Healthllm.md (152)
  Contract with Heritage Life Assurance for Lifellm.md (100)
  Contract with Lakeshore Mutual for Bizllm.md (51)
  Contract with Metropolitan Life Group for Lifellm.md (199)
  Contract with National Claims Network for Claimllm.md (182)
  Contract with Pinnacle Insurance Co. for Homellm.md (39)
  Contract with Premier Adjusters Inc. for Claimllm.md (123)
  ... +9 more files
knowledge-base/employees/
  Alex Chen.md (47)
  Alex Harper.md (58)
  Alex Thomson.md (37)
  Amanda Foster.md (67)
  Avery Lancaster.md (64)
  Brandon Walker.md (47)
  Carlos Rodriguez.md (55)
  Daniel Park.md (51)
  David Kim.md (47)
  Dmitri Volkov.md (35)
  Emily Carter.md (49)
  Emily Tran.md (73)
  Hannah Ortiz.md (32)
  James Wilson.md (70)
  Jennifer Adams.md (41)
  Jessica Liu.md (50)
  Jordan Blake.md (35)
  Jordan K. Bishop.md (38)
  Kevin Zhang.md (51)
  Lisa Anderson.md (55)
  Marcus Johnson.md (52)
  Maxine Thompson.md (54)
  Maya Thompson.md (46)
  Michael O'Brien.md (63)
  Michelle Rivera.md (55)
  ... +9 more files
knowledge-base/memos/
  Annual Operations Review 2024.md (63)
  Company Newsletter Q3 2025.md (18)
  Healthllm Customer FAQ (Draft).md (23)
  Sales Pipeline Summary Q3 2025.md (19)
  Support Ticket Export Cascade Mutual.md (27)
  Vendor Security Review Log.md (12)
knowledge-base/policies/
  Expense Reimbursement Policy v1.4.md (21)
  Expense Reimbursement Policy v2.0.md (22)
  Information Security Policy v3.1.md (25)
  Information Security Policy v4.0.md (30)
  Leave and Time Off Policy.md (23)
  Remote Work Policy 2022.md (17)
  Remote Work Policy 2025.md (21)
knowledge-base/products/
  Bizllm.md (59)
  Carllm.md (67)
  Claimllm.md (62)
  Healthllm.md (56)
  Homellm.md (45)
  Lifellm.md (52)
  Markellm.md (55)
  Rellm.md (60)
scripts/
  codemap.py (190)
tests/
  test_evaluator.py (85)
  test_stress_dataset.py (41)
```

_Symbols: install universal-ctags (`ctags`) to include them._
<!-- END GENERATED -->
