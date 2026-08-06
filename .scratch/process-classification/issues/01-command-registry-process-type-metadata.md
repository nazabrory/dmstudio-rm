# 01 — Command Registry Process Type Metadata & Domain Glossary

**What to build:**
Expose a structured `process_type` (`"file_based"` vs `"interactive"`) on every command dictionary returned by `dmstudio.command_registry` functions (`list_commands`, `get_command_schema`, `search_commands`). Update `CONTEXT.md` with canonical domain terms for file-based vs. interactive processes.

**Blocked by:** None — can start immediately

**Status:** completed

- [x] Define `INTERACTIVE_COMMANDS` index in `dmstudio.command_registry`.
- [x] Add `process_type` key (`"file_based"` or `"interactive"`) to `list_commands()`, `get_command_schema()`, and `search_commands()` outputs.
- [x] Add definitions for `File-based process` and `Interactive process` to `CONTEXT.md`.
- [x] Add unit test in `tests/test_workflow.py` validating `process_type` metadata retrieval.
