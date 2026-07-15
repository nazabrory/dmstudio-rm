# AGENTS.md - dmstudio Development Guide

## Project Overview

Python package for Datamine Studio RM scripting via Windows COM automation. 
The package source lives in `dmstudio/` (a subfolder of the project root `dmstudio-rm3/`). The project root contains packaging config, examples, tests, and setup scripts.

---

## 🛠️ Project Preparation & Setup (For Developers & Agents)

To run tests or examples, the environment must be configured as follows:
1. **Windows & Datamine Studio RM**: Must be running on a Windows system with Datamine Studio RM installed and licensed.
2. **Open Project**: Open **`Project.rmproj`** in Datamine Studio RM before executing any script that interacts with COM.
3. **Environment Setup**:
   ```bash
   # Option A: Standard venv setup (creates .venv, installs deps, installs package editable)
   setup_env.bat        # CMD (one-click setup)
   .\setup_env.ps1      # PowerShell (one-click setup)

   # Option B: Conda environment setup
   conda create --name dmstudio python=3.9 -y
   conda activate dmstudio
   conda install -y pandas numpy nbformat -c conda-forge
   pip install pywin32 mcp
   pip install -e .
   ```
4. **Active COM Session**: The COM library connects to the running instance of Studio RM. Keep the application open with `Project.rmproj` active.

---

## 🏗️ File Structure

```
dmstudio-rm3/                     ← Project root (working directory for scripts)
├── dmstudio/                     ← Python package source
│   ├── __init__.py               ← Package entrypoint exporting all submodules
│   ├── version.py                ← Version string ('2.0-beta')
│   ├── initialize.py             ← COM initialization; supports StudioRM3.x dynamically
│   ├── dmcommands.py             ← ~265 auto-generated command wrappers
│   ├── dmfiles.py                ← File-generation commands (INPFIL etc.)
│   ├── special.py                ← COM automation helpers
│   ├── superprocess.py           ← Multi-command workflows (dxf_to_dm, display_ellipsoids)
│   ├── agent.py                  ← AI agent helpers (schema, file reader, dialog dismissal)
│   └── notebook_builder.py       ← Jupyter Notebook builder
├── mcp_server.py                 ← FastMCP stdio server
├── tutorials/                    ← Tutorials and Datamine project files
│   ├── Project.rmproj            ← Your Datamine project file
│   ├── Holes3D_Tutorial.ipynb    ← Drillhole de-survey workflow notebook
│   ├── Studio_RM_3.1_Examples.ipynb ← Jupyter examples notebook
│   └── Database/                 ← Raw tutorial database files
├── tests/                        ← Centralized developer test and helper scripts
│   ├── quick_test.py             ← Smoke test (no Studio license needed)
│   ├── test_workflow.py          ← Verification script (Notebook, Command schema, search tests)
│   ├── integration_test.py       ← Integration test suite
│   ├── stress_test.py            ← End-to-end COM test (requires active Studio + project)
│   ├── diagnose_project.py       ← Studio connection diagnostic utility
│   └── generate_wrappers.py      ← Regenerates dmcommands.py from StudioRM.chm XML
├── requirements.txt              ← Pinned dependencies
├── pyproject.toml                ← Modern packaging config
└── setup.py                      ← Legacy setup (kept for compatibility)
```

---

## 🤖 AI Agent & MCP Specifications

### `dmstudio/agent.py`
AI agent helper module. Import: `from dmstudio import agent`

| Function | Description |
|----------|-------------|
| `agent.list_commands()` | Returns all 265 Datamine commands as `[{name, doc}]` |
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
