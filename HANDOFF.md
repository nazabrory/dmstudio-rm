# HANDOFF.md — dmstudio Project Handoff

**Last updated:** 2026-07-15  
**Status:** ✅ AI Agent & MCP Upgrade Complete, Decluttered, and Organized

---

## 1. What This Project Is

`dmstudio` is a Python package that automates [Datamine Studio RM](http://www.dataminesoftware.com) via Windows COM automation (`pywin32`). It was forked from the original open-source project by Sean Horan (MIT licence) and extended with:

- Full AI agent tooling (command discovery, native file reading, dialog management)
- Jupyter Notebook builder for auditable workflows
- Model Context Protocol (MCP) server for Claude Desktop / Antigravity integration
- Studio RM 3.3+ version compatibility

The project workspace has been decluttered to be highly intuitive for geologists. All developer test and helper scripts have been centralized in the `tests/` folder. All examples have been converted to interactive Jupyter Notebooks.

---

## 2. Architecture Overview

```
dmstudio-rm3/                     ← project root (working directory for scripts)
├── dmstudio/                     ← Python package
│   ├── __init__.py               ← exports all submodules
│   ├── version.py                ← version string '2.0-beta'
│   ├── initialize.py             ← COM init; supports StudioRM3.x dynamically
│   ├── dmcommands.py             ← ~265 auto-generated command wrappers
│   ├── dmfiles.py                ← file-generation commands (INPFIL etc.)
│   ├── special.py                ← COM automation helpers
│   ├── superprocess.py           ← multi-command workflows (dxf_to_dm, display_ellipsoids)
│   ├── agent.py                  ← AI agent helpers (see below)
│   └── notebook_builder.py       ← Jupyter Notebook builder
├── mcp_server.py                 ← FastMCP stdio server
├── examples/
│   └── Studio_RM_3.1_Examples.ipynb ← ★ NEW: Jupyter examples notebook
├── Holes3D_Tutorial.ipynb        ← drillhole de-survey workflow notebook
├── tests/                        ← ★ CENTRALIZED: Developer test and helper scripts
│   ├── quick_test.py             ← smoke test (no Studio license needed)
│   ├── test_workflow.py          ← verification script
│   ├── integration_test.py       ← integration test suite
│   ├── stress_test.py            ← end-to-end COM test (requires Studio + project)
│   ├── diagnose_project.py       ← Studio connection diagnostic utility
│   └── generate_wrappers.py      ← regenerates dmcommands.py from StudioRM.chm XML
├── requirements.txt              ← pinned dependencies
├── pyproject.toml                ← modern packaging config
└── setup.py                      ← legacy setup (kept for compatibility)
```

---

## 3. New Modules (This Session)

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
# Then execute: jupyter nbconvert --to notebook --execute --inplace workflow.ipynb
```

### `mcp_server.py`
FastMCP stdio server. Run: `.venv\Scripts\python mcp_server.py`

MCP tools exposed:
- `list_commands` — all Datamine commands
- `get_command_schema(command_name)` — parameter signature
- `read_datamine_file(filepath, max_rows)` — file preview as JSON
- `create_jupyter_workflow(notebook_name, steps)` — builds `.ipynb` from step list

**To register with Claude Desktop** (`%APPDATA%\Claude\claude_desktop_config.json`):
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

**To register with Antigravity** (`.gemini/config/antigravity.json` or via IDE settings):
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

## 4. Critical COM Engineering Rules

Always keep these in mind when extending COM automation:

1. **Backslashes break `Parsecommand()`** — never pass Windows paths directly as command arguments. Register files first via `ActiveProject.AddFile(absolute_path)` and use the logical name.

2. **Spaces in paths break the parser** — same root cause. The CLI parser splits on spaces. Use `AddFile()` to sidestep this.

3. **Leading underscore = scratch (in-memory) file** — Datamine does NOT write `_tempfile` to disk. Use `tempfile` (no underscore) to verify on-disk output.

4. **Blocking modals** — `Parsecommand()` runs on the main thread and will hang if Studio shows a `#32770` dialog. Use `agent.dialog_dismiss_context()` (opt-in) or the `win32gui` pattern in `stress_test.py`.

5. **COM ProgID is version-agnostic** — all `StudioRM3.x` versions share `Datamine.StudioRM.Application`. The version string in `initialize.studio()` is metadata only.

6. **`DmFile.DmTableADO` fields are 1-indexed** — `Schema.GetFieldName(1)` is the first field.

---

## 5. How to Run Verification

All tests should be run from the root directory but execute self-contained modules located in the `tests/` directory:

### Smoke test (no Studio needed)
```bash
.venv\Scripts\python tests\quick_test.py
```

### Full verification (no Studio needed)
```bash
.venv\Scripts\python tests\test_workflow.py
```

### End-to-end COM stress test (requires active Studio RM + `Project.rmproj`)
```bash
.venv\Scripts\python tests\stress_test.py
```

---

## 6. Next Steps for Future Agents

- [ ] **MCP tool execution** — verify end-to-end MCP workflow creation tools with an active Studio session.
- [ ] **Pytest conversion** — migrate the standalone test files in `tests/` into proper `pytest` formatted test cases.
- [ ] **Type hinting** — add type annotations to `dmstudio/agent.py` and `dmstudio/notebook_builder.py`.

---

## 7. Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `pywin32` | ≥227 | COM automation |
| `numpy` | ≥1.20 | Numerical ops |
| `pandas` | ≥1.3 | DataFrames |
| `nbformat` | ≥5.0 | Notebook JSON writing |
| `mcp` | ≥1.0 | MCP stdio server |

Install: `.venv\Scripts\pip install -r requirements.txt`

---

## 8. Licence

Original work © 2018 Sean D. Horan — MIT Licence.  
Modifications and new contributions © 2025 nazabrory contributors — MIT Licence.  
`LICENSE.txt` must be included in all distributions.
