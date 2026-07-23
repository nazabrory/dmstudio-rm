# Context: dmstudio

Ubiquitous language for the dmstudio package: Studio RM automation, package surface, and notebook verification.

## Language

### Product surface

**Command wrapper**:
A Python method on `dmcommands.init` or `dmfiles.init` that builds a Studio CLI string and sends it via COM `Parsecommand`.
_Avoid_: macro, process method (when you mean the Python API)

**Approved command wrapper**:
A command wrapper that has been tested inside the sandbox environment and verified to execute successfully without raising python validation errors, COM errors, or triggering blocking interactive dialog popups.


**Process command**:
A Studio process exposed through `dmcommands` (e.g. sort, copy, holes3d) — roughly one sandbox under `tutorials/collections/processes/`.
_Avoid_: file command (those live under `dmfiles`)

**File command**:
A Studio file-generation or directory utility exposed through `dmfiles` (e.g. INPFIL, PROTOM) — sandboxes under `tutorials/collections/files/`.
_Avoid_: process command

**Active project**:
The Datamine project currently open in the running Studio RM instance; COM automation targets this workspace and its folder.
_Avoid_: working directory (Python cwd may differ until aligned)

**Scratch file**:
A Datamine logical name with a leading underscore; kept in memory and not written to disk as a normal project file.
_Avoid_: temp file (unless you mean an on-disk name without `_`)

**Canonical module**:
The module that implements a capability today (`command_registry`, `dm_io`, `dialog`, `bootstrap`, `sandbox`). Prefer importing from here in new code and docs.
_Avoid_: treating `agent` as the implementation home

**Compat re-export**:
The `agent` module’s public surface that re-exports helpers from canonical modules so older scripts and notebooks keep working.
_Avoid_: “agent owns I/O / discovery / dialogs” as current architecture

### Notebook testing

**Test sandbox**:
An isolated workspace directory with a single Datamine project (`Project.rmproj`) used to run notebooks without multi-project COM conflicts.
_Avoid_: temporary folder (generic OS temp)

**Notebook runner**:
The coordinator that runs notebooks sequentially in a test sandbox: project checks, path patching, dialog dismissal, timeouts, and post-run cleanup.
_Avoid_: nbconvert alone (when you mean the full orchestration)

**Test results**:
Timestamped storage of a run’s summary (`summary.md`) and failing/errored evaluated notebooks.
_Avoid_: output folder (unspecified)

### EXTRA Process Syntax

**EXTRA Expression List**:
A Python list of string transformation statements passed to `dm_cmd.extra(in_i=..., out_o=..., expression=[...])`.
- String constants **must use double quotes** (`"VAL"`).
- New numeric fields require `;N` (`VAL;N = 10.0`). New string fields require `;A<len>` (`CODE;A16 = "STR"`).
- Reserved characters or functions used as field names must be enclosed in brackets (`[g/t]`, `[max]`).
- Conditional statements must use `elseif` (one word) and end with `end`.
- Missing values must be tested using `absent()` function (`IF (AU == ABSENT()) ...`).
- Fields referenced in `prev()`, `next()`, or arithmetic expressions must exist or be calculated in earlier lines.
- Temporary scratch fields can be removed before output with `erase(FIELD)`.

