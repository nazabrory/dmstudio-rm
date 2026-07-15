# HANDOFF.md — dmstudio Project Handoff

**Last updated:** 2026-07-15  
**Status:** ✅ AI Agent & MCP Upgrade Complete

---

## 1. What This Project Is

`dmstudio` is a Python package that automates [Datamine Studio RM](http://www.dataminesoftware.com) via Windows COM automation (`pywin32`). It was forked from the original open-source project by Sean Horan (MIT licence) and extended with:

- Full AI agent tooling (command discovery, native file reading, dialog management)
- Jupyter Notebook builder for auditable workflows
- Model Context Protocol (MCP) server for Claude Desktop / Antigravity integration
- Studio RM 3.3+ version compatibility

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
│   ├── agent.py                  ← ★ NEW: AI agent helpers (see below)
│   └── notebook_builder.py       ← ★ NEW: Jupyter Notebook builder
├── mcp_server.py                 ← ★ NEW: FastMCP stdio server
├── examples/
│   └── studio_rm_31_example.py   ← usage examples
├── Holes3D_Tutorial.ipynb        ← drillhole de-survey workflow notebook
├── scratch/                      ← dev/test scripts (gitignored)
│   ├── test_workflow.py          ← verification script (run to check everything works)
│   ├── clean_notebook.py         ← one-time SLR reference cleaner (already run)
│   ├── test_parse.py             ← parser unit tests
│   └── test_parse_adv.py         ← advanced parser tests
├── quick_test.py                 ← smoke test (no Studio license needed)
├── stress_test.py                ← end-to-end COM test (requires Studio + project)
├── diagnose_project.py           ← Studio connection diagnostic utility
├── generate_wrappers.py          ← regenerates dmcommands.py from StudioRM.chm XML
├── integration_test.py           ← integration test suite
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

## 5. How to Verify Everything Works

### Smoke test (no Studio needed)
```bash
.venv\Scripts\python quick_test.py
```

### Full verification (no Studio needed)
```bash
.venv\Scripts\python scratch\test_workflow.py
```
Expected output:
- `[1]` NotebookBuilder → OK, 8 cells
- `[2]` list_commands → OK, 265 commands
- `[3]` get_command_schema("copy") → OK
- `[4]` search_commands("sort") → OK, finds mgsort
- `[5]` StudioRM3.x resolution → all True

### End-to-end COM stress test (requires active Studio RM + `Project.rmproj`)
```bash
.venv\Scripts\python stress_test.py
```

### Run the Holes3D tutorial notebook
```bash
# With venv jupyter (after installing jupyter):
.venv\Scripts\pip install jupyter
.venv\Scripts\jupyter notebook Holes3D_Tutorial.ipynb

# Or with nbconvert:
.venv\Scripts\jupyter nbconvert --to notebook --execute --inplace Holes3D_Tutorial.ipynb
```

---

## 6. Next Steps for Future Agents

### High Priority
- [ ] **MCP registration** — register `mcp_server.py` in the user's Antigravity or Claude Desktop config and validate all 4 tools end-to-end with a live Studio RM session
- [ ] **Regenerate wrappers from 3.3 help file** — if a `StudioRM.chm` from version 3.3 is available, run `generate_wrappers.py` to pick up any new commands
- [ ] **`agent.read_datamine()` test** — validate against a live `.dm` file with the `DmFile.DmTableADO` COM path once Studio is running

### Medium Priority
- [ ] **Add a `tests/` directory** — convert `scratch/test_workflow.py` to a proper `pytest` suite
- [ ] **Example notebook for MCP workflow** — create `examples/mcp_agent_workflow.ipynb` showing an AI agent building and executing a Jupyter notebook via MCP tools
- [ ] **`agent.resolve_path_arguments()`** — implement the planned helper that auto-calls `AddFile()` for path args before running a command

### Low Priority
- [ ] Update `examples/studio_rm_31_example.py` to showcase the new agent and notebook_builder APIs
- [ ] Add type hints to `agent.py` and `notebook_builder.py` (new files, safe to annotate)

---

## 7. Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `pywin32` | ≥227 | COM automation |
| `numpy` | ≥1.20 | Numerical ops |
| `pandas` | ≥1.3 | DataFrames |
| `nbformat` | ≥5.0 | Notebook JSON writing |
| `mcp` | ≥1.0 | MCP stdio server |
| `nbconvert` | any | Notebook execution (dev) |

Install: `.venv\Scripts\pip install -r requirements.txt`

---

## 8. Git History (Recent)

| Commit | Message |
|--------|---------|
| *(next)* | `feat: AI agent module, MCP server, NotebookBuilder, Studio RM 3.3+ support` |
| `c2b43ef` | feat: add support and documentation for Studio RM 3.2 |
| `b7560a5` | Add Holes3D_Tutorial.ipynb and enable .dmx mapping |
| `49db50b` | Refactor parser, regenerate processes, add COM stress testing |
| `1af896e` | Add AGENTS.md, integration test, and project diagnostics |

---

## 9. Licence

Original work © 2018 Sean D. Horan — MIT Licence.  
Modifications and new contributions © 2025 nazabrory contributors — MIT Licence.  
`LICENSE.txt` must be included in all distributions.
