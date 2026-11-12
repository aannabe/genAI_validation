# Python Coding Template

A Python-only starter repository for coding with AI agents. It includes a uv-based Python
toolchain, agent instructions, on-demand skills, and a code map. No example application code is
included; add project code under `python/` and tests under `python/tests/`.

## Quick start

1. Copy this repo (or use it as a GitHub template).
2. Rename the placeholder project `myproject` in `pyproject.toml`.
3. Add Python code under `python/` and tests under `python/tests/`.
4. Run `uv sync`, then `uv run ruff check .`, `uv run ruff format --check .`, and
   `uv run pytest`.
5. Refresh the code map with `uv run --no-project scripts/codemap.py`.

## Layout

```
AGENTS.md                         shared instructions for every agent
CLAUDE.md, GEMINI.md              pointers to AGENTS.md
.github/copilot-instructions.md   Copilot pointer
.agents/skills/<name>/SKILL.md    on-demand Python and task guidance
.claude/skills -> ../.agents/skills   link so Claude Code finds the same skills
.vscode/settings.json             Copilot terminal approvals
.claude/settings.json             Claude Code permissions
docs/CODEMAP.md                   compact repository map
python/                           Python source files and tests
pyproject.toml, uv.lock           uv, Ruff, and pytest configuration
scripts/codemap.py                Python code-map generator
```

## How it works

- **AGENTS.md** is short and always loaded: principles, workflow, "ask first" boundaries,
  and token-saving habits. Rules are advisory.
- **Skills** hold detail and load only when relevant. The Python skill covers project conventions;
  task skills cover `code-review`, `testing`, `debugging`, `git-workflow`, `security`,
  `refactoring`, and `docs-and-codemap`.
- **Guardrails:** agents may lint, test, and run read-only git commands freely. They must ask
  before `git commit/push`, `gh`, adding dependencies, installs, or deletions. These are set in
  the VS Code and Claude settings; if VS Code ignores workspace-level rules, copy that block to
  your User Settings.
- **Iteration:** agents verify their changes and retry up to 5 times, then report.

## Switching or adding an AI provider

| Provider | Reads | Skills from |
|---|---|---|
| Copilot (VS Code, CLI, cloud agent) | `AGENTS.md`, `.github/copilot-instructions.md` | `.agents/skills` |
| Claude Code | `CLAUDE.md` (imports `AGENTS.md`) | `.claude/skills` (link) |
| Gemini CLI / VS Code agent | `GEMINI.md` (imports `AGENTS.md`) | `.agents/skills` |
| Codex and others | `AGENTS.md` | `.agents/skills` |

To support a new tool: if it reads `AGENTS.md` natively, do nothing. Otherwise add a one-line
pointer file for it, like `CLAUDE.md`. Instructions stay in one place.

## Token efficiency and indexing

- Copilot builds a semantic code index automatically. GitHub-hosted repos are indexed once on
  GitHub; for repos not on GitHub, VS Code builds the index by uploading workspace data to
  GitHub (see GitHub's repository-indexing docs). Command: *Build Codebase semantic index*.
- `docs/CODEMAP.md` gives agents a compact map of files and symbols, while `AGENTS.md` encourages
  searching before reading. `scripts/codemap.py` uses only the Python standard library;
  universal-ctags can add top-level symbols.
- Skills load on demand; keep `AGENTS.md` short.

## Platform notes (macOS, Linux, Windows)

- Use `uv` for Python commands and `pathlib` plus list-style `subprocess` calls for portable code.
- `.claude/skills` is a symlink. On Windows either enable Developer Mode and
  `git config core.symlinks true` before cloning, or ignore it: `CLAUDE.md`/`AGENTS.md` tell
  Claude to read `.agents/skills/` directly, and Copilot and Gemini do not need the link.
