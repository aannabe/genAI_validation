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
| Markdown | 14 | 402 |
| Python | 1 | 190 |
| JSON | 2 | 61 |
| Other | 4 | 60 |
| TOML | 1 | 26 |

### Files (line counts)

```
./
  .editorconfig (15)
  .gitattributes (5)
  .gitignore (19)
  AGENTS.md (61)
  CLAUDE.md (6)
  GEMINI.md (4)
  LICENSE (21)
  README.md (72)
  pyproject.toml (26)
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
  settings.json (26)
docs/
  CODEMAP.md (78)
scripts/
  codemap.py (190)
```

_Symbols: install universal-ctags (`ctags`) to include them._
<!-- END GENERATED -->
