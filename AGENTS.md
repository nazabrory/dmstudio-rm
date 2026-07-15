# AGENTS.md - dmstudio Development Guide

## Project Overview

Python package for Datamine Studio RM scripting via Windows COM automation. The package source lives in `dmstudio/dmstudio/`; the outer `dmstudio/` is the project root containing packaging config, examples, and setup scripts.

## Commands

### Setup Environment
```bash
# Windows - one-click setup (creates .venv, installs deps, installs package editable)
dmstudio/setup_env.bat        # CMD
dmstudio/setup_env.ps1        # PowerShell

# Manual setup
cd dmstudio
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

### Run Verification
```bash
# Smoke test (no Studio license required)
cd dmstudio
python quick_test.py
```

### Run Examples
```bash
cd dmstudio
python examples/studio_rm_31_example.py   # Requires active Studio license
```

### Install / Rebuild
```bash
cd dmstudio
pip install -e .          # Editable install (dev)
pip install .             # Standard install
python setup.py build     # Legacy build
```

### No Test Suite Yet
There is no pytest/unittest suite. `quick_test.py` is the only verification script. When adding tests, create `dmstudio/tests/` and use pytest.

### No Linter/Formatter Configured
No ruff, black, flake8, or mypy config exists. Follow existing code style (see below). If adding tooling, use ruff for linting+formatting and mypy for type checking.

## Code Style

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
- Max line length: ~120 chars (existing code exceeds this in places; don't reflow)
- No trailing semicolons (remove if adding new code)

### Type Hints
- **None currently used.** The codebase is untyped.
- If adding type hints, use them sparingly on new public functions. Do not retrofit existing code.

### Docstrings
- Use triple-single-quoted block docstrings for classes and methods
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
- Use `raise ValueError("message")` for invalid parameters
- Use `raise RuntimeError("message")` for initialization failures
- Sentinel pattern: default params to `"required"` or `"optional"`, then check:
  ```python
  if param == "required":
      raise ValueError("param is required.")
  if param != "optional":
      command += " *param=" + param
  ```
- Avoid bare `except:` — use `except Exception as e:` (existing code has a few bare excepts; fix if touching)
- Use `assert` for preconditions in helper functions (e.g., `assert dxf_i.lower().endswith('.dxf')`)

### Datamine Command String Syntax
When building command strings for `oScript.Parsecommand()`:
- `&` prefix for files: `&infile=filename`
- `*` prefix for fields: `*field=FIELDNAME`
- `@` prefix for parameters: `@param=value`
- `{}` for retrieval criteria: `{RETRIEVAL_STRING}`

### pandas Compatibility
- **pandas 3.0+ breaking change:** `pd.DataFrame(scalar_dict)` fails. Always wrap in list: `pd.DataFrame([scalar_dict])`
- Use `pd.concat()` instead of deprecated `DataFrame.append()`

### COM Automation
- Initialize once via `dmstudio.initialize.studio('StudioRM')` and reuse
- Supported versions: `'Studio3'`, `'StudioRM'`, `'StudioRM3.1'`, `'StudioRM3.2'`, `'StudioEM'`
- Python `win32com.client.Dispatch()` is unaffected by Studio RM 3.1 & 3.2's "safer scripting" restrictions (those only block JavaScript `new ActiveXObject()` patterns)

## File Structure
```
dmstudio/                          # Project root
├── dmstudio/                      # Python package (source)
│   ├── __init__.py                # Re-exports submodules
│   ├── version.py                 # __version__ = '2.0-beta'
│   ├── initialize.py              # COM initialization, dmdir.py generation
│   ├── dmcommands.py              # ~45k lines, auto-generated command wrappers
│   ├── dmfiles.py                 # ~1.2k lines, file-generation commands
│   ├── special.py                 # Helpers, dmfile_def, inpfil, automation
│   └── superprocess.py            # Multi-command workflows
├── examples/                      # Usage examples
├── quick_test.py                  # Smoke test
├── pyproject.toml                 # Packaging config
├── requirements.txt               # Pinned deps
├── setup.py                       # Legacy setup
├── setup_env.bat / .ps1           # Environment setup scripts
└── .venv/                         # Virtual environment (git-ignored)
```

## Key Gotchas
- `dmcommands.py` is auto-generated from StudioRM.chm — do not manually reformat
- `dmdir.py` and root `__init__.py` are generated at runtime by `_make_dmdir()` — do not commit
- Windows-only: depends on `pywin32` and Datamine Studio COM objects
- No cross-platform support
