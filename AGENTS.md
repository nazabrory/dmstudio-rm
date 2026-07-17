# AGENTS.md - dmstudio Development Guide

## Project Overview

Python package for Datamine Studio RM scripting via Windows COM automation. 
The package source lives in `dmstudio/` (a subfolder of the project root `dmstudio/`). The project root contains packaging config, examples, tests, and setup scripts.

---

## 🛠️ Project Preparation & Setup (For Developers & Agents)

To run tests or examples, the environment must be configured as follows:
1. **Windows & Datamine Studio RM**: Must be running on a Windows system with Datamine Studio RM installed and licensed.
2. **Open Project**: Open **`Project.rmproj`** in Datamine Studio RM before executing any script that interacts with COM.
3. **Environment Setup**:
   ```bash
   # Option A: Conda environment setup (Recommended)
   # Assumes conda is installed. Uses the environment.yml file.
   conda env create -f environment.yml
   conda activate dmstudio
   pip install -e .

   # Option B: Standard venv setup via uv (Fast alternative)
   # Assumes uv is installed.
   uv venv
   .venv\Scripts\activate
   uv pip install -r requirements.txt
   uv pip install -e .
   uv pip install jupyterlab

   # Option C: Legacy PowerShell/CMD setup scripts
   setup_env.bat        # CMD (one-click setup)
   .\setup_env.ps1      # PowerShell (one-click setup)
   ```
4. **Active COM Session**: The COM library connects to the running instance of Studio RM. Keep the application open with `Project.rmproj` active.

---

## 🏗️ File Structure

```
dmstudio-rm3/                     ← Project root (working directory for scripts)
├── dmstudio/                     ← Python package source
│   ├── __init__.py               ← Package entrypoint exporting all submodules
│   ├── version.py                ← Version string ('2.0.0b3')
│   ├── initialize.py             ← COM initialization; supports StudioRM3.x dynamically
│   ├── dmcommands.py             ← ~270 auto-generated command wrappers
│   ├── dmfiles.py                ← ~30 file-generation command wrappers (INPFIL etc.)
│   ├── special.py                ← COM automation helpers
│   ├── superprocess.py           ← Multi-command workflows (dxf_to_dm, display_ellipsoids)
│   ├── agent.py                  ← AI agent helpers (schema, file reader, dialog dismissal)
│   └── notebook_builder.py       ← Jupyter Notebook builder
├── mcp_server.py                 ← FastMCP stdio server
├── tutorials/                    ← Tutorials and Datamine project files
│   ├── Project.rmproj            ← Shared tutorial project file
│   ├── collections/              ← Process & file-command workspace collection
│   │   ├── processes/            ← One sandbox per dmcommands wrapper (~268 folders)
│   │   │   ├── copy/
│   │   │   │   ├── Project.rmproj
│   │   │   │   └── copy_example.ipynb
│   │   │   ├── holes3d/
│   │   │   │   ├── Project.rmproj
│   │   │   │   └── holes3d_example.ipynb
│   │   │   └── ... (all other process folders)
│   │   └── files/                ← One sandbox per dmfiles wrapper (~32 folders)
│   │       ├── protom/
│   │       │   ├── Project.rmproj
│   │       │   └── protom_example.ipynb
│   │       ├── inpfil/
│   │       │   ├── Project.rmproj
│   │       │   └── inpfil_example.ipynb
│   │       └── ... (all other file-command folders)
│   └── case_studies/             ← End-to-end tutorial workflows
│       ├── holes3d_desurvey/
│       │   ├── Project.rmproj
│       │   └── Holes3D_Tutorial.ipynb
│       ├── grade_estimation/
│       │   ├── Project.rmproj
│       │   └── Grade_Estimation_Examples.ipynb
│       └── studio_rm_examples/
│           ├── Project.rmproj
│           └── Studio_RM_3.1_Examples.ipynb
├── tests/                        ← Centralized developer test and helper scripts
│   ├── quick_test.py             ← Smoke test (no Studio license needed)
│   ├── test_workflow.py          ← Verification script (Notebook, Command schema, search tests)
│   ├── integration_test.py       ← Integration test suite
│   ├── stress_test.py            ← End-to-end COM test (requires active Studio + project)
│   ├── diagnose_project.py       ← Studio connection diagnostic utility
│   ├── run_sandbox_tests.py      ← Automated sequential validation runner for notebooks
│   ├── generate_wrappers.py      ← Regenerates dmcommands.py from StudioRM.chm XML
│   ├── generate_collections.py   ← Regenerates all 300 process/file sandbox notebooks
│   └── restructure_case_studies.py ← Migrates case study notebooks to case_studies/
├── requirements.txt              ← Pinned dependencies
├── pyproject.toml                ← Modern packaging config
└── setup.py                      ← Legacy setup (kept for compatibility)
```

---

## 🤖 AI Agent & MCP Specifications

### Local Handoffs & Workspace Context
To support persistent context and session handovers across different AI coding tools (such as Google Antigravity, Cursor, Roo Code, Claude Code, GitHub Copilot):
- **Local Handover Directory:** Always write session-specific handoff reports, planning notes, or temporary scratchpad scripts to the `.agents/` directory in the repository root.
- **Gitignored:** The `.agents/` folder is explicitly gitignored in `.gitignore`, keeping the main codebase repository history clean.
- **Accessing History:** Future AI agents should scan this directory for recent `.md` reports (e.g. `handoff_report.md`) to read previous session outcomes and continue workflows seamlessly.

### `dmstudio/agent.py`
AI agent helper module. Import: `from dmstudio import agent`

| Function | Description |
|----------|-------------|
| `agent.list_commands()` | Returns all 300 Datamine commands as `[{name, doc}]` |
| `agent.get_command_schema(cmd)` | Returns full parameter schema for a command |
| `agent.search_commands(query)` | Fuzzy keyword search across command names/docs |
| `agent.read_datamine(filepath)` | Reads `.dm`/`.dmx` binary into pandas DataFrame via `DmFile.DmTableADO` COM |
| `agent.dialog_dismiss_context()` | Context manager: background thread dismisses blocking `#32770` Studio dialogs |

### `dmstudio/notebook_builder.py`
Programmatic Jupyter Notebook generator. Import: `from dmstudio.notebook_builder import NotebookBuilder`

```python
nb = NotebookBuilder('workflow.ipynb', title='My Workflow')
nb.add_markdown('## Step 1')
nb.add_code("cmd.mgsort(in_i='collars', out_o='sorted', keys_f=['BHID'])")
nb.save()
```

### `mcp_server.py`
FastMCP stdio server. Run: `.venv\Scripts\python mcp_server.py`

Exposed MCP tools:
- `list_commands` — returns all Datamine commands
- `get_command_schema(command_name)` — returns parameter signature
- `read_datamine_file(filepath, max_rows)` — returns file preview as JSON
- `create_jupyter_workflow(notebook_name, steps)` — builds `.ipynb` from a step list

#### Registering MCP with Claude Desktop (`%APPDATA%\Claude\claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "dmstudio": {
      "command": "D:\\OnGoing Project\\dmstudio-rm3\\.venv\\Scripts\\python",
      "args": ["D:\\OnGoing Project\\dmstudio-rm3\\mcp_server.py"]
    }
  }
}
```

#### Registering MCP with Antigravity (`.gemini/config/antigravity.json`):
```json
{
  "mcpServers": {
    "dmstudio": {
      "command": "D:\\OnGoing Project\\dmstudio-rm3\\.venv\\Scripts\\python",
      "args": ["D:\\OnGoing Project\\dmstudio-rm3\\mcp_server.py"]
    }
  }
}
```

---

## Agent skills

### Issue tracker

Issues and PRDs for this repo live as GitHub issues. See [issue-tracker.md](file:///D:/Active/dmstudio/docs/agents/issue-tracker.md).

### Triage labels

Triage labels map directly to canonical roles: needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix. See [triage-labels.md](file:///D:/Active/dmstudio/docs/agents/triage-labels.md).

### Domain docs

Single-context repository layout (one CONTEXT.md + docs/adr/ at repo root). See [domain.md](file:///D:/Active/dmstudio/docs/agents/domain.md).

---

## 🛠️ Verification & Commands

### Run Smoke Test (no Studio license required)
```bash
.venv\Scripts\python tests\quick_test.py
```

### Run Full Verification (no Studio license required)
```bash
.venv\Scripts\python tests\test_workflow.py
```

### Run Connection Diagnostic (requires active Studio + loaded project)
```bash
.venv\Scripts\python tests\diagnose_project.py
```

### Run End-to-End COM Stress Test (requires active Studio + loaded project)
```bash
.venv\Scripts\python tests\stress_test.py
```

### Rebuild / Reinstall (Editable mode)
```bash
.venv\Scripts\pip install -e .
```

---

## 📏 Code Style Guide

### Imports
- Standard library first, then third-party, then local (blank line between groups)
- Use absolute imports within the package: `from dmstudio import dmcommands`
- Module-level `OSCRYPTCON = None` pattern for COM connection caching

### Naming Conventions
- **Parameters follow Datamine CLI semantics:**
  - `_i` suffix = input file (e.g., `in_i`)
  - `_o` suffix = output file (e.g., `out_o`)
  - `_f` suffix = field name (e.g., `zone_f`)
  - `_p` suffix = parameter value (e.g., `allrecs_p`)
  - `retrieval` = retrieval criteria string
- Classes: `PascalCase` (`dmfile_def`, `init`)
- Functions/methods: `snake_case` (`run_command`, `parse_infields_list`)
- Constants: `UPPER_SNAKE_CASE` (`OSCRYPTCON`, `CHAR8_FIELDS`, `IMPLICIT_FIELDS`)
- Private/internal: leading underscore (`_scriptinit`, `_make_dmdir`)

### Formatting
- **No formatter configured** — match existing style
- Single quotes preferred for strings (`'required'`, `'optional'`)
- Triple single quotes for docstrings (`'''docstring'''`)
- 4-space indentation
- Max line length: ~120 chars (do not reflow existing auto-generated commands)
- No trailing semicolons

### Type Hints
- **None currently used** (codebase is untyped).
- If adding type hints, use them sparingly on new public functions. Do not retrofit existing code.

### Docstrings
- Use triple-single-quoted block docstrings for classes and methods.
- Format:
  ```
  '''
  FUNCTION_NAME
  -------------
  Description text.

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
- Auto-generated commands in `dmcommands.py` use this format — preserve it.

### Error Handling
- Use `raise ValueError("message")` for invalid parameters.
- Use `raise RuntimeError("message")` for initialization failures.
- Sentinel pattern: default params to `"required"` or `"optional"`, then check:
  ```python
  if param == "required":
      raise ValueError("param is required.")
  if param != "optional":
      command += " *param=" + param
  ```
- Avoid bare `except:` — use `except Exception as e:`.
- Use `assert` for preconditions in helper functions (e.g., `assert dxf_i.lower().endswith('.dxf')`).

### Datamine Command String Syntax
When building command strings for `oScript.Parsecommand()`:
- `&` prefix for files: `&infile=filename`
- `*` prefix for fields: `*field=FIELDNAME`
- `@` prefix for parameters: `@param=value`
- `{}` for retrieval criteria: `{RETRIEVAL_STRING}`

### pandas Compatibility
- **pandas 3.0+ breaking change:** `pd.DataFrame(scalar_dict)` fails. Always wrap in list: `pd.DataFrame([scalar_dict])`
- Use `pd.concat()` instead of deprecated `DataFrame.append()`

---

## ⚡ Critical COM Engineering Rules

Always keep these in mind when extending COM automation:

1. **Backslashes break `Parsecommand()`** — never pass Windows paths directly as command arguments. Register files first via `ActiveProject.AddFile(absolute_path)` and use the logical name.
2. **Spaces in paths break the parser** — same root cause. The CLI parser splits on spaces. Use `AddFile()` to sidestep this.
3. **Leading underscore = scratch (in-memory) file** — Datamine does NOT write `_tempfile` to disk. Use `tempfile` (no underscore) to verify on-disk output.
4. **Blocking modals** — `Parsecommand()` runs on the main thread and will hang if Studio shows a `#32770` dialog. Use `agent.dialog_dismiss_context()` (opt-in) or the `win32gui` pattern in `stress_test.py`.
5. **COM ProgID is version-agnostic** — all `StudioRM3.x` versions share `Datamine.StudioRM.Application`. The version string in `initialize.studio()` is metadata only.
6. **`DmFile.DmTableADO` fields are 1-indexed** — `Schema.GetFieldName(1)` is the first field.
7. **`dmdir.py` and root `__init__.py`** are generated at runtime by `_make_dmdir()`. Do not commit them to Git.

---

## 🏷️ Versioning Policy (PEP 440 Compliance)

When modifying or releasing this package, future AI agents and developers must strictly follow standard PEP 440 version rules:
1. **Pre-release Naming**: Avoid non-standard descriptors like `2.0-beta-patch` or `2.0.0-beta.1` in configuration scripts. Instead, use normalized PEP 440 pre-release notation:
   - First beta: `2.0.0b0` (or `2.0b0`)
   - Patch / update on that beta: `2.0.0b1` (or `2.0b1`), `2.0.0b2`, etc.
2. **Release Naming**: Standard semantic version tags for production releases: `2.0.0`, `2.0.1` (patch), `2.1.0` (minor), etc.
3. **Locations**: Whenever the package version is updated, update both:
   - `dmstudio/version.py` (`__version__ = 'X.Y.Z'`)
   - `CHANGELOG.md` heading (e.g. `## X.Y.Z (Title) - YYYY-MM-DD`)
