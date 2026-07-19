# Changelog

## 2.0.0b12 - 2026-07-19

- **Wrapper Consolidation**: Consolidated unverified command wrappers from `dmcommands_generated.py` and `dmfiles_generated.py` directly into `dmcommands.py` and `dmfiles.py`. Added user warnings when unverified wrappers are called.
- **Simplified Command Discovery**: Removed fallback imports from `command_registry.py` for generated modules.
- **Sandbox Improvements**: Updated `sandbox.py` to automatically regenerate local `dmdir.py` files in sandbox folders.

## 2.0.0b11 - 2026-07-19

- **AI Setup Integration**: Embedded the unified `dmstudio` Agent rules (`agent_rules.md`) directly in the package data.
- **MCP Rules & Prompts**: Added a dedicated MCP Resource (`resource://dmstudio/agent-rules`) and Prompt (`dmstudio-rules`) to allow automatic context injection into AI clients.
- **Workspace Skills Installer**: Introduced `--install-skills` CLI option and `dmstudio.install_agent_skills()` helper to install coding skills to local `.agents/skills/` workspaces.
- **Interactive Setup Prompt**: Tailored the README setup guide around a single copy-paste prompt instructing AI assistants to automatically build local JSON MCP configurations and workspace skills.

## 2.0.0b10 - 2026-07-19

- **Version Bump**: Bumped pre-release version to 2.0.0b10.

## 2.0.0b9 (IDE Settings Guide & Documentation) - 2026-07-18

- **`README.md` & `SKILL.md`**: Enhanced environment and MCP installation documentation to explicitly guide Cursor, Windsurf, and other IDE users on manual graphical settings setup, since these editors do not utilize Claude Desktop's JSON configuration.

## 2.0.0b8 (Workspace Skill Copying via CLI) - 2026-07-18

- **`mcp_server.py`**: Added copy logic to `--install` that copies packaged skills (`dmstudio/skills/`) directly to the user's project directory `.agents/skills/` so AI assistants running in custom workspaces automatically discover, index, and follow the instructions.
- **`pyproject.toml`**: Configured `package-data` to include all skills markdown files (`skills/**/*.md`) inside the built wheel.

## 2.0.0b7 (AI Skill Indexing and Package Integration) - 2026-07-18

- **`.gitignore`**: Unignored `.agents/skills/` directory to allow IDEs and AI tools to index and discover agent skills.
- **`dmstudio/__init__.py`**: Embedded the automated environment preparation instructions and COM isolation policy directly into the package's top-level docstring so that they are visible even when installed via PyPI without a repository clone.

## 2.0.0b6 (Automated MCP Installer & COM-less Server) - 2026-07-18

- **`mcp_server.py`**: Added `--install` CLI argument to automatically detect environment python path and register with Claude Desktop, plus print other IDE configurations. Removed COM dependencies and the `read_datamine_file` tool to enforce strict COM isolation.
- **`.agents/skills/prepare-env/SKILL.md`**: Created new agent skill for environment preparation, automated MCP server installation, and outlining COM isolation boundary.
- **`README.md` & `AGENTS.md`**: Documented automated environment setup capability, the `--install` CLI flag, and the COM isolation rules.

## Documentation & module layout (current as of 2.0.0b4) - 2026-07-17

Docs-only alignment with the split package surface (no behaviour change):

| Capability | Canonical module | Compat re-export |
|------------|------------------|------------------|
| `list_commands`, `get_command_schema`, `search_commands` | `command_registry` | `agent` |
| `read_datamine`, `to_datamine`, `patch_dataframe` | `dm_io` | `agent` |
| `dialog_dismiss_context` | `dialog` | `agent` |
| `download_tutorials` | `bootstrap` | `agent`, `dmstudio.download_tutorials` |
| Sandbox helpers | `sandbox` | `agent` |

- **`README.md`**: Thin dual-audience guide (users first); Conda-first install; compact architecture; canonical imports with one-line `agent` compat note; tutorials table including `custom_notebooks/`.
- **`AGENTS.md`**: Full module map, MCP tool list (includes `search_commands`), placeholder paths, COM rules cite `dialog` first.
- **`CONTEXT.md`**: Product surface glossary plus notebook-testing terms.
- Historical entries below keep original release narrative; annotations note **where code lives now** when names moved.

---

## 2.0.0b4 (Tutorials Restructuring & Split Collections) - 2026-07-16

### Structural Changes
- **Split Process Collections:** Refactored `tutorials/collections/` into two clearly separated subfolders:
  - **`tutorials/collections/processes/`** — One self-contained sandbox per `dmcommands` wrapper (~268 folders).
  - **`tutorials/collections/files/`** — One self-contained sandbox per `dmfiles` wrapper (~32 folders).
- **Case Studies Directory:** Moved all end-to-end tutorial notebooks out of the `tutorials/` root into a new **`tutorials/case_studies/`** directory:
  - `case_studies/holes3d_desurvey/` — Full Holes3D drillhole de-surveying workflow.
  - `case_studies/grade_estimation/` — Complete ESTIMA + COKRIG grade estimation workflow.
  - `case_studies/studio_rm_examples/` — Advanced Studio RM 3.1+ scripting examples.
- **Portable Relative Paths:** Updated all case study notebooks to replace hardcoded `D:\Active\dmstudio\...` paths with `os.path.abspath(os.path.join(...))` relative path resolution, making them portable across machines and clones.
- **Case-Insensitive Project Verification:** All case study notebooks now use `.lower()` normalization on `ActiveProject.Folder` and `notebook_folder` to prevent false failures on Windows drive-letter case differences.
- **Cleaned `tutorials/` Root:** Removed all loose `.dmx` scratch files, temporary outputs, and standalone notebooks from the tutorials root, leaving only `Project.rmproj` and the organized subdirectories.

### Generator Updates
- **`generate_collections.py`:** Updated to output notebooks to `processes/` or `files/` subdirectories (based on whether the command is in `dmcommands` or `dmfiles`). Also handles copying and updating the three special pre-built custom notebooks (`protom`, `estima`, `cokrig`) with portable paths. Old flat-directory notebooks are cleaned up automatically at the end of a run.
- **`restructure_case_studies.py`:** New helper script in `tests/` that migrates the three root-level case study notebooks to `tutorials/case_studies/`, normalizes paths, and removes obsolete root-level files.

### Documentation
- **`AGENTS.md`:** Updated file structure tree to reflect the new `processes/`, `files/`, and `case_studies/` layout.
- **`README.md`:** Updated tutorial run instructions to point users to `tutorials/case_studies/` first, then the `collections/processes/` and `collections/files/` reference sandboxes.

## 2.0.0b3 (Process Example Notebook Collection & Introspection Upgrade) - 2026-07-16

### Features
- **Unified Introspection for `dmfiles`:** Extended command discovery (originally surfaced via `agent`; **now implemented in `command_registry`**, re-exported by `agent`) to inspect both `dmcommands.init` and `dmfiles.init`. All ~300 Datamine commands (including `protom` and `inpfil`) are discoverable, searchable, and schema-extractable.
- **Process Example Notebook Collection:** Created `generate_collections.py` to programmatically generate process example notebooks and directories under `tutorials/collections/`.
  - **Frictionless Portability:** Uses relative resolution paths to automatically locate the Datamine help database from the collections directory, ensuring zero setup issues when cloned.
  - **Case-Insensitive Windows Pathing:** Normalized ActiveProject folder comparisons using `.lower()` to prevent drive letter case mismatches on Windows.
  - **Docstring-Aware parameter requirement logic:** Evaluates whether a list or scalar input file is marked as compulsory (`Required=Yes`) inside the process's docstring and uncomments it automatically (e.g. `samples_i` in `holes3d` or `inmods_i` in `desurv` are now active).
  - **Thorough Workspace Cleanup:** Upgraded the notebooks' final cell to remove generated `dmdir.py`, `__init__.py`, and `__pycache__` artifacts in addition to `t_` prefix files, restoring directory layouts to "as new" states.
  - **Interactive HTML Results Verification:** Output cells read and display previews of actual computed output files using `agent.read_datamine` (**canonical: `dm_io.read_datamine`**, re-exported by `agent`).

## 2.0.0b2 (Interactive Visualization & COM Fixes) - 2026-07-16

### Bug Fixes
- **`agent.read_datamine` / table read path:** Fixed a critical bug in the Datamine table reader (shipped under `agent`; **now lives in `dm_io`**) where it called `table.GetValue(i)` instead of the correct ADO COM method `table.GetColumn(i)`, returning `None` for all values.
- **`dm.compdh` wrapper:** Corrected input file syntax prefix from `&**in**=` to `&in=` in `dmcommands.py`.
- **`dm.join` wrapper:** Exposed `keys_f` field parameter mapping inside the `join` method signature in `dmcommands.py`.

### Workflow & Visualization Enhancements
- **Interactive 3D WebGL (Plotly):** Bypassed experimental Python 3.14 + Conda on Windows fatal crashes (`0xc06d007f` in `numpy.linalg.inv`) during 3D plotting by introducing a standalone, interactive 3D WebGL HTML plot using **Plotly.js (via CDN)**. The plot is embedded inline inside JupyterLab using `IPython.display.IFrame`, avoiding C++ extension segmentation faults entirely.
- **File Locking Workaround:** Avoided Datamine write locks by copying `comp_holes.dmx` to a temporary copy dynamically located using `oScript.ActiveProject.Folder`, reading it with pandas, cleaning up the copy, and then loading it into the active Datamine 3D view window.

### Testing & Diagnostics
- **Integration Tests:** Patched `tests/integration_test.py` and `tests/diagnose_project.py` to support newer Studio RM COM project properties (`.Title` and `.Folder`) while retaining safe fallbacks to legacy `.Name` and `.Directory`.
- **Package Dependencies:** Added `matplotlib` to `environment.yml` and `requirements.txt`.

## 2.0.0b1 (Conda Support, VS Code Agents & Root Cleanup) - 2026-07-15

### Clean Workspace
- Centralized all project files (`Project.rmproj`), tutorial databases (`Database/`), tutorial notebooks (`Holes3D_Tutorial.ipynb`, `Studio_RM_3.1_Examples.ipynb`), and scratch `.dmx` tables into a clean `tutorials/` subdirectory.
- Removed deprecated/temporary run-time files (`dmdir.py`, root `__init__.py`) and empty `examples/` directory from the root directory to maintain a tidy project workspace.

### Conda Integration
- Added full support and instructions for Anaconda/Miniconda environments (`conda create -n dmstudio python=3.9`).
- Configured Conda environment setup details in both `README.md` and `AGENTS.md`.

### VS Code & Direct AI Agent Guidelines
- Documented how VS Code coding agents (like Cursor, Github Copilot, Roo Code, Claude Code) can natively interact with the repository without the need for an MCP server, utilizing direct workspace access and reading `.dm` data files via `agent.read_datamine` (**canonical: `dm_io.read_datamine`**).
- Added detailed steps on configuring Jupyter Notebook kernels inside VS Code to directly edit and execute the generated notebooks.

### Disclaimer & License Terms
- Added an official disclaimer in `README.md` clarifying that the library is unofficial and community-maintained, and does not violate Datamine terms since it operates on official COM APIs with a valid user license.

## 2.0-beta (AI Agent & MCP Upgrade)

### Studio RM 3.3+ Compatibility
- `initialize.studio()` now dynamically resolves any `StudioRM3.x` version string (e.g. `StudioRM3.3`, `StudioRM3.4`), future-proofing version support beyond the previously hard-coded 3.2.
- Replaced bare `except:` blocks in `initialize.py` with `except Exception:` (PEP-8 best practice).

### AI Agent Module (`dmstudio/agent.py`) — new file
Originally introduced as the home of AI helpers. **Later split into canonical modules**; `agent` remains a **compat re-export** layer:

- `list_commands()` — **now `command_registry`**
- `get_command_schema(cmd_name)` — **now `command_registry`**
- `search_commands(query)` — **now `command_registry`**
- `read_datamine(filepath)` — **now `dm_io`**
- `dialog_dismiss_context()` — **now `dialog`**

### Jupyter Notebook Builder (`dmstudio/notebook_builder.py`) — new file
- `NotebookBuilder(filename, title)` — Programmatically builds auditable Jupyter Notebooks.
- Methods: `add_markdown(text)`, `add_code(code)`, `save()`.
- AI agents should write all workflows to notebooks (via `NotebookBuilder`) for full auditability, then execute with `jupyter nbconvert --to notebook --execute --inplace`.

### MCP Server (`mcp_server.py`) — new file
- FastMCP stdio server; originally four tools, **now five**: `list_commands`, `get_command_schema`, `search_commands`, `read_datamine_file`, `create_jupyter_workflow`.
- Compatible with Claude Desktop, Google Antigravity, and any MCP-capable client.

### Cleanup: Removed SLR / Sean Horan References
- `README.md` — Removed author attribution, updated copyright to generic, added AI/MCP documentation.
- `pyproject.toml` — Removed `authors` entry (Sean Horan / rpacan.com).
- `setup.py` — Removed `author` / `author_email` fields.
- `dmstudio/superprocess.py` — Removed `pyrpa` import and "only available to SLR employees" messages. Rewrote `display_ellipsoids` to use `agent.read_datamine()` (**canonical: `dm_io.read_datamine`**).
- `Holes3D_Tutorial.ipynb` — Stripped SLR employee stdout from output cells.

### Package Updates
- `dmstudio/__init__.py` — Exports new `agent` and `notebook_builder` submodules (later also canonical modules and `download_tutorials`).
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
