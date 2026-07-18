# AGENTS.md - dmstudio Development Guide

## Project Overview

Python package for Datamine Studio RM scripting via Windows COM automation.
The package source lives in `dmstudio/`. The project root holds packaging config, tutorials, tests, MCP server, and setup scripts.

User-facing install and quick start: **[README.md](README.md)**. Domain vocabulary: **[CONTEXT.md](CONTEXT.md)**.

---

## Project Preparation & Setup

1. **Windows & Datamine Studio RM**: Windows with Studio RM installed and licensed.
2. **Open Project**: Open a `.rmproj` (e.g. `tutorials/test_sandbox/Project.rmproj`) in Studio RM before any COM script.
3. **Environment Setup** (Conda recommended):
   ```bash
   # Option A: Conda (recommended)
   conda env create -f environment.yml
   conda activate dmstudio
   pip install -e .

   # Option B: uv
   uv venv
   .venv\Scripts\activate
   uv pip install -r requirements.txt
   uv pip install -e .
   uv pip install jupyterlab

   # Option C: One-click Windows helpers
   setup_env.bat        # CMD
   .\setup_env.ps1      # PowerShell
   ```
4. **Active COM Session**: The library attaches to the running Studio RM instance. Keep Studio open with the intended project active.

---

## File Structure

```
dmstudio-rm/                      ← Project root
├── dmstudio/                     ← Python package source
│   ├── __init__.py               ← Exports submodules; download_tutorials shortcut
│   ├── version.py                ← Version string ('2.0.0b4')
│   ├── initialize.py             ← COM init; StudioRM3.x dynamic resolution
│   ├── dmcommands.py             ← ~268 process command wrappers
│   ├── dmfiles.py                ← ~32 file-command wrappers (INPFIL, PROTOM, …)
│   ├── command_registry.py       ← list_commands / get_command_schema / search_commands
│   ├── dm_io.py                  ← read_datamine / to_datamine (DataFrame ↔ .dm/.dmx)
│   ├── dialog.py                 ← dialog_dismiss_context (Win32 modal dismisser)
│   ├── bootstrap.py              ← download_tutorials
│   ├── sandbox.py                ← Sandbox / dataset copy helpers
│   ├── agent.py                  ← Compat re-export layer (see below)
│   ├── special.py                ← Adapted COM helpers
│   ├── superprocess.py           ← Multi-command workflows
│   └── notebook_builder.py       ← Jupyter Notebook builder
├── mcp_server.py                 ← FastMCP stdio server
├── tutorials/
│   ├── Project.rmproj            ← Project template (used by restructure_case_studies)
│   ├── test_sandbox/             ← Isolated runtime sandbox for running notebooks
│   │   └── Project.rmproj        ← Active project file to open in Studio RM
│   ├── Database/                 ← Tutorial source data
│   ├── collections/              # All single-command notebooks (flat list)
│   └── workflows/                # All multi-command workflows and case studies
│       ├── holes3d_desurvey/
│       ├── grade_estimation/
│       ├── studio_rm_examples/
│       └── ai_agent_workflow_tutorial.ipynb
├── tests/
│   ├── quick_test.py
│   ├── test_workflow.py
│   ├── integration_test.py
│   ├── stress_test.py
│   ├── diagnose_project.py
│   ├── run_sandbox_tests.py
│   ├── generate_wrappers.py
│   ├── generate_collections.py
│   └── restructure_case_studies.py
├── requirements.txt
├── environment.yml
├── pyproject.toml
├── setup.py
├── setup_env.bat / setup_env.ps1
├── start_jupyter.bat
├── README.md
├── AGENTS.md
├── CONTEXT.md
└── CHANGELOG.md
```

### Repository Layout Decisions

To maintain codebase simplicity and a clean experience for the user:
- **Root-level setup and launch scripts** (`setup_env.bat`, `setup_env.ps1`, `start_jupyter.bat`) and `mcp_server.py` are explicitly placed in the root directory. This makes the package highly accessible to Windows automation users by offering immediate "first-click" environment setup and starting Jupyter Lab directly at the workspace root.
- **Excluded Runtime Files**: Local files `dmdir.py` and the root `__init__.py` are created dynamically during execution by `_make_dmdir()` and are git-ignored. Developers should keep the root clean by deleting these files when not running scripts.

---

## Package surface (canonical vs compat)

### Canonical modules

| Module | Role | Key API |
|--------|------|---------|
| `dmcommands` | Process command wrappers | `dmcommands.init()` |
| `dmfiles` | File-generation wrappers | `dmfiles.init()` |
| `initialize` | COM / Studio / DmFile bootstrap | `studio()`, `dmFile()` |
| `command_registry` | Discovery without side effects of full agent import | `list_commands()`, `get_command_schema()`, `search_commands()` |
| `dm_io` | Binary table I/O via `DmFile.DmTableADO` | `read_datamine()`, `to_datamine()`, `patch_dataframe()` |
| `dialog` | Opt-in modal dismissal | `dialog_dismiss_context()` |
| `bootstrap` | Tutorial download | `download_tutorials(target_dir)` (also `dmstudio.download_tutorials`) |
| `sandbox` | Sandbox dataset helpers | `copy_database_files()`, `initialize_sandbox()` |
| `notebook_builder` | Programmatic `.ipynb` | `NotebookBuilder` |
| `special` / `superprocess` | Extra COM workflows | e.g. `dxf_to_dm`, plot/PDF helpers |

### `dmstudio/agent.py` (compat re-export)

Import: `from dmstudio import agent`.

**Does not own implementations.** Re-exports for backward compatibility:

| Symbol | Canonical home |
|--------|----------------|
| `list_commands`, `get_command_schema`, `search_commands` | `command_registry` |
| `read_datamine`, `to_datamine`, `patch_dataframe` | `dm_io` |
| `dialog_dismiss_context` | `dialog` |
| `copy_database_files`, `initialize_sandbox` | `sandbox` |
| `download_tutorials` | `bootstrap` |

Prefer **canonical modules** in new code and docs. Tutorials/tests may still use `agent.*`.

### `dmstudio/notebook_builder.py`

```python
from dmstudio.notebook_builder import NotebookBuilder
nb = NotebookBuilder('workflow.ipynb', title='My Workflow')
nb.add_markdown('## Step 1')
nb.add_code("cmd.mgsort(in_i='collars', out_o='sorted', keys_f=['BHID'])")
nb.save()
```

### `mcp_server.py`

Run: `.venv\Scripts\python mcp_server.py` (or Conda env python).

MCP tools (via `command_registry`, `dm_io`, `NotebookBuilder`):

- `list_commands`
- `get_command_schema(command_name)`
- `search_commands(query)`
- `read_datamine_file(filepath, max_rows)`
- `create_jupyter_workflow(notebook_name, steps)`

#### Claude Desktop (`%APPDATA%\Claude\claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "dmstudio": {
      "command": "C:\\path\\to\\dmstudio-rm\\.venv\\Scripts\\python.exe",
      "args": ["C:\\path\\to\\dmstudio-rm\\mcp_server.py"]
    }
  }
}
```

#### Antigravity (example)

```json
{
  "mcpServers": {
    "dmstudio": {
      "command": "C:\\path\\to\\dmstudio-rm\\.venv\\Scripts\\python.exe",
      "args": ["C:\\path\\to\\dmstudio-rm\\mcp_server.py"]
    }
  }
}
```

---

## Local handoffs

- Write session handoff notes / scratch plans under **`.agents/`** (gitignored).
- Scan that folder for recent handoffs when resuming work across tools.

---

## Agent skills (repo docs)

- Issue tracker: [docs/agents/issue-tracker.md](docs/agents/issue-tracker.md)
- Triage labels: [docs/agents/triage-labels.md](docs/agents/triage-labels.md)
- Domain docs layout: [docs/agents/domain.md](docs/agents/domain.md)

---

## Verification & commands

### No Studio license required

```bash
.venv\Scripts\python tests\quick_test.py
.venv\Scripts\python tests\test_workflow.py
```

### Active Studio + loaded project

```bash
.venv\Scripts\python tests\diagnose_project.py
.venv\Scripts\python tests\stress_test.py
.venv\Scripts\python tests\integration_test.py
.venv\Scripts\python tests\run_sandbox_tests.py
```

### Rebuild editable install

```bash
.venv\Scripts\pip install -e .
```

### Generators

- **`tests/generate_wrappers.py`** — regenerates `dmcommands.py` from StudioRM help XML.
- **`tests/generate_collections.py`** — regenerates sandbox notebooks under `tutorials/collections/`.
- **`tests/restructure_case_studies.py`** — workflows/case-studies layout helper (migration).

---

## Code style guide

### Imports

- Stdlib → third-party → local (blank line between groups)
- Absolute package imports: `from dmstudio import dmcommands`
- Prefer canonical modules over `agent` for new code

### Naming

- Parameters follow Datamine CLI semantics:
  - `_i` = input file (`in_i`)
  - `_o` = output file (`out_o`)
  - `_f` = field name (`zone_f`)
  - `_p` = parameter (`allrecs_p`)
  - `retrieval` = retrieval criteria string
- Classes: `PascalCase` (`dmfile_def`, `init`)
- Functions: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Private: leading `_`

### Formatting

- No formatter configured — match existing style
- Single quotes preferred; triple single quotes for docstrings
- 4-space indent; ~120 char lines; do not reflow auto-generated `dmcommands.py`

### Type hints

- Codebase largely untyped; add sparingly on new public APIs only

### Docstrings

Triple-single-quoted blocks; auto-generated command style:

```
'''
FUNCTION_NAME
-------------
Description.

Parameters:
-----------
param_name: type
    Description.

Returns:
--------
return_type
    Description.
'''
```

### Error handling

- `ValueError` for bad params; `RuntimeError` for init failures
- Sentinel `"required"` / `"optional"` pattern in wrappers
- Avoid bare `except:`; use `except Exception as e:`
- `assert` for helper preconditions where already used

### Datamine command string syntax

- `&` files: `&infile=filename`
- `*` fields: `*field=FIELDNAME`
- `@` params: `@param=value`
- `{}` retrieval: `{RETRIEVAL_STRING}`

### pandas

- pandas 3+: wrap scalar dicts: `pd.DataFrame([scalar_dict])`
- Prefer `pd.concat` over deprecated `DataFrame.append`

---

## Critical COM engineering rules

1. **Backslashes break `Parsecommand()`** — do not pass Windows paths as command args. Use `ActiveProject.AddFile(absolute_path)` then logical names.
2. **Spaces in paths break the parser** — same fix: `AddFile()`.
3. **Leading underscore = scratch file** — not written to disk; use non-`_` names for durable outputs.
4. **Blocking modals** — `Parsecommand()` is main-thread; hang risk. Prefer `dialog.dialog_dismiss_context()` (also available as `agent.dialog_dismiss_context` re-export) or the `win32gui` pattern in `stress_test.py`.
5. **COM ProgID is version-agnostic** — `Datamine.StudioRM.Application`; version string in `initialize.studio()` is metadata.
6. **`DmFile.DmTableADO` fields are 1-indexed** — `Schema.GetFieldName(1)` is first field.
7. **`dmdir.py` and runtime root `__init__.py`** from `_make_dmdir()` — do not commit.

---

## Versioning policy (PEP 440)

1. Pre-releases: `2.0.0b0`, `2.0.0b1`, … (not `2.0-beta-patch`).
2. Releases: `2.0.0`, `2.0.1`, `2.1.0`, …
3. On version bump update:
   - `dmstudio/version.py` (`__version__`)
   - `pyproject.toml` `[project].version`
   - `CHANGELOG.md` heading
