# Changelog

## 2.0.0b2 (Interactive Visualization & COM Fixes) - 2026-07-16

### Bug Fixes
- **`agent.read_datamine`:** Fixed a critical bug in [dmstudio/agent.py](file:///D:/OnGoing%20Project/dmstudio-rm3/dmstudio/agent.py#L241) where it was calling `table.GetValue(i)` instead of the correct ADO COM method `table.GetColumn(i)`, returning `None` for all values.
- **`dm.compdh` wrapper:** Corrected input file syntax prefix from `&**in**=` to `&in=` in [dmstudio/dmcommands.py](file:///D:/OnGoing%20Project/dmstudio-rm3/dmstudio/dmcommands.py#L6806).
- **`dm.join` wrapper:** Exposed `keys_f` field parameter mapping inside the `join` method signature in [dmstudio/dmcommands.py](file:///D:/OnGoing%20Project/dmstudio-rm3/dmstudio/dmcommands.py).

### Workflow & Visualization Enhancements
- **Interactive 3D WebGL (Plotly):** Bypassed experimental Python 3.14 + Conda on Windows fatal crashes (`0xc06d007f` in `numpy.linalg.inv`) during 3D plotting by introducing a standalone, interactive 3D WebGL HTML plot using **Plotly.js (via CDN)**. The plot is embedded inline inside JupyterLab using `IPython.display.IFrame`, avoiding C++ extension segmentation faults entirely.
- **File Locking Workaround:** Avoided Datamine write locks by copying `comp_holes.dmx` to a temporary copy dynamically located using `oScript.ActiveProject.Folder`, reading it with pandas, cleaning up the copy, and then loading it into the active Datamine 3D view window.

### Testing & Diagnostics
- **Integration Tests:** Patched [tests/integration_test.py](file:///D:/OnGoing%20Project/dmstudio-rm3/tests/integration_test.py) and [tests/diagnose_project.py](file:///D:/OnGoing%20Project/dmstudio-rm3/tests/diagnose_project.py) to support newer Studio RM COM project properties (`.Title` and `.Folder`) while retaining safe fallbacks to legacy `.Name` and `.Directory`.
- **Package Dependencies:** Added `matplotlib` to [environment.yml](file:///D:/OnGoing%20Project/dmstudio-rm3/environment.yml) and [requirements.txt](file:///D:/OnGoing%20Project/dmstudio-rm3/requirements.txt).

## 2.0.0b1 (Conda Support, VS Code Agents & Root Cleanup) - 2026-07-15


### Clean Workspace
- Centralized all project files (`Project.rmproj`), tutorial databases (`Database/`), tutorial notebooks (`Holes3D_Tutorial.ipynb`, `Studio_RM_3.1_Examples.ipynb`), and scratch `.dmx` tables into a clean `tutorials/` subdirectory.
- Removed deprecated/temporary run-time files (`dmdir.py`, root `__init__.py`) and empty `examples/` directory from the root directory to maintain a tidy project workspace.

### Conda Integration
- Added full support and instructions for Anaconda/Miniconda environments (`conda create -n dmstudio python=3.9`).
- Configured Conda environment setup details in both `README.md` and `AGENTS.md`.

### VS Code & Direct AI Agent Guidelines
- Documented how VS Code coding agents (like Cursor, Github Copilot, Roo Code, Claude Code) can natively interact with the repository without the need for an MCP server, utilizing direct workspace access and reading `.dm` data files via `agent.read_datamine`.
- Added detailed steps on configuring Jupyter Notebook kernels inside VS Code to directly edit and execute the generated notebooks.

### Disclaimer & License Terms
- Added an official disclaimer in `README.md` clarifying that the library is unofficial and community-maintained, and does not violate Datamine terms since it operates on official COM APIs with a valid user license.

## 2.0-beta (AI Agent & MCP Upgrade)

### Studio RM 3.3+ Compatibility
- `initialize.studio()` now dynamically resolves any `StudioRM3.x` version string (e.g. `StudioRM3.3`, `StudioRM3.4`), future-proofing version support beyond the previously hard-coded 3.2.
- Replaced bare `except:` blocks in `initialize.py` with `except Exception:` (PEP-8 best practice).

### AI Agent Module (`dmstudio/agent.py`) — new file
- `list_commands()` — Returns all dmcommands wrappers as a JSON-serialisable list.
- `get_command_schema(cmd_name)` — Returns full parameter schema for a command.
- `search_commands(query)` — Fuzzy keyword search over command names and docstrings.
- `read_datamine(filepath)` — Reads `.dm`/`.dmx` binary files into pandas DataFrames using `DmFile.DmTableADO` COM object — no proprietary dependencies.
- `dialog_dismiss_context()` — Opt-in context manager that auto-dismisses blocking `#32770` Studio RM modal dialogs in a background thread.

### Jupyter Notebook Builder (`dmstudio/notebook_builder.py`) — new file
- `NotebookBuilder(filename, title)` — Programmatically builds auditable Jupyter Notebooks.
- Methods: `add_markdown(text)`, `add_code(code)`, `save()`.
- AI agents should write all workflows to notebooks (via `NotebookBuilder`) for full auditability, then execute with `jupyter nbconvert --to notebook --execute --inplace`.

### MCP Server (`mcp_server.py`) — new file
- FastMCP stdio server exposing 4 tools: `list_commands`, `get_command_schema`, `read_datamine_file`, `create_jupyter_workflow`.
- Compatible with Claude Desktop, Google Antigravity, and any MCP-capable client.

### Cleanup: Removed SLR / Sean Horan References
- `README.md` — Removed author attribution, updated copyright to generic, added AI/MCP documentation.
- `pyproject.toml` — Removed `authors` entry (Sean Horan / rpacan.com).
- `setup.py` — Removed `author` / `author_email` fields.
- `dmstudio/superprocess.py` — Removed `pyrpa` import and "only available to SLR employees" messages. Rewrote `display_ellipsoids` to use `agent.read_datamine()`.
- `Holes3D_Tutorial.ipynb` — Stripped SLR employee stdout from output cells.

### Package Updates
- `dmstudio/__init__.py` — Exports new `agent` and `notebook_builder` submodules.
- `requirements.txt` — Added `nbformat>=5.0.0`, updated `mcp>=1.0.0`.
- `pyproject.toml` — Added `nbformat` and `mcp` to package dependencies.



### Studio RM 3.2 Support
- Added explicit support for Datamine Studio RM 3.2 via the `'StudioRM3.2'` version string in `initialize.py`.
- Updated boilerplate templates in `generate_wrappers.py` and regenerated both `dmcommands.py` and `dmfiles.py`.
- Updated `AGENTS.md` developer documentation to include Studio RM 3.2.

### Jupyter Notebook Interface
- Added `Holes3D_Tutorial.ipynb` implementing the complete drillhole de-surveying workflow from the Datamine scripting tutorial.
- Configured local environment integration to execute Datamine processes interactively in Jupyter.
- Included export of final drillhole database table to CSV and reading in Pandas.

### Improvements & Bug Fixes
- Fixed a method casing bug in `dmstudio/special.py` by renaming `oScript.ParseCommand` to `oScript.Parsecommand` to match the exact COM object definition.
- Modified `_make_dmdir()` in `dmstudio/initialize.py` to match both `.dm` and `.dmx` extensions to correctly map XML database files in the project workspace.
- Copied tutorial database files (`_vb_assays.dmx`, `_vb_collars.dmx`, `_vb_lithology.dmx`, `_vb_surveys.dmx`) to the project folder to enable direct Datamine access.
- Updated `examples/studio_rm_31_example.py` to document UI-based command execution (like `update-scripts`) via the generic `run_command` interface.

## 2.0-beta

### New Commands (Studio RM 3.1)
- `copymod` - Copy block model with retrieval criteria support
- `update_scripts` - Batch convert scripts to safer syntax
- `digitise_doughnut` - Create closed strings with internal voids
- `smooth_gradient` - Full smoothing of preselected strings
- `set_view_fov` - Set default field of view angle
- `switch_drillhole_points_traces` - Toggle drillhole display mode
- `intext` - Text import with optional INDD/SETTINGS files

### Updated Commands
- `compdh` - Now supports up to 5 ZONE fields and 5 DOM fields for dominant categorical values
- `modsplit` - MODELOUT and FULLMOD outputs are now optional (can output one or both)

### Automation Helpers (Studio RM 3.1)
- `special.print_plot_sheet_to_pdf()` - Print plot sheets to PDF via COM
- `special.text_importer()` - Run Text Importer via COM using scenario files
- `special.create_isoshells()` - Create isoshells via COM with name-value pairs

### Bug Fixes
- Fixed 15+ auto-generation variable name mismatches in `dmcommands.py`
- Fixed `dmfiles.comres` zone field reference bug
- Fixed `dmfiles.py` bare except clause
- Fixed `special.py` invalid raise statement (Python 3 compatibility)
- Fixed deprecated `pandas.DataFrame.append()` usage
- Fixed deprecated `numpy.str.split()` usage
- Fixed `np.str.split` in `superprocess.py`

### Improvements
- Added `pyproject.toml` for modern Python packaging
- Updated `setup.py` with current repository URL and README reference
- Added Studio RM 3.1 version support in initialization
- Added safer scripting documentation/comments
- Added example script: `examples/studio_rm_31_example.py`
- Updated README with version support and changelog
- Bumped version to 2.0-beta
