# Changelog

## 2.0-beta (2026-07-15 Update)

### Jupyter Notebook Interface
- Added `Holes3D_Tutorial.ipynb` implementing the complete drillhole de-surveying workflow from the Datamine scripting tutorial.
- Configured local environment integration to execute Datamine processes interactively in Jupyter.
- Included export of final drillhole database table to CSV and reading in Pandas.

### Improvements & Bug Fixes
- Modified `_make_dmdir()` in `dmstudio/initialize.py` to match both `.dm` and `.dmx` extensions to correctly map XML database files in the project workspace.
- Copied tutorial database files (`_vb_assays.dmx`, `_vb_collars.dmx`, `_vb_lithology.dmx`, `_vb_surveys.dmx`) to the project folder to enable direct Datamine access.

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
