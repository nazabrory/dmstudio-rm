# Context: dmstudio Notebook Testing Domain

This document defines the ubiquitous language and domain concepts for the `dmstudio` Jupyter notebook verification system.

## Glossary

### test_sandbox
A dedicated, isolated workspace directory containing a single Datamine project (`Project.rmproj`). It is used to execute Jupyter notebooks sequentially, avoiding COM automation conflicts arising from having multiple projects open in Datamine Studio RM simultaneously.

### notebook_runner
The programmatic execution coordinator that runs notebooks sequentially in the `test_sandbox`. It is responsible for:
- Verifying the active project matching.
- Dynamically patching relative database paths.
- Auto-dismissing blocking Studio RM dialogs in a background thread.
- Managing execution timeouts.
- Wiping all sandbox files (excluding the project metadata) after each run.

### test_results
The storage location for test execution outputs. Each run generates a timestamped subfolder containing a markdown summary report (`summary.md`) and evaluated `.ipynb` notebook files for any runs that encountered errors or failed.
