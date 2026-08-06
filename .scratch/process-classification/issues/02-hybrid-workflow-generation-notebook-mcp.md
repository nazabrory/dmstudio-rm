# 02 — Hybrid Workflow Generation (NotebookBuilder & MCP Server)

**What to build:**
Enable `NotebookBuilder` and `mcp_server.create_jupyter_workflow` to recognize interactive commands and automatically generate Markdown human-instruction checkpoint cells (guidance for 3D viewport picking in Studio RM) accompanied by file verification code cells.

**Blocked by:** 01 — Command Registry Process Type Metadata & Domain Glossary

**Status:** completed

- [x] Update `NotebookBuilder` step processing to check command `process_type`.
- [x] Format interactive steps as Markdown instruction cells with step-by-step Studio RM viewport instructions and output file verification code.
- [x] Expose updated step schemas and tool descriptions in `mcp_server.py`.
- [x] Add integration test in `tests/test_workflow.py` verifying hybrid notebook generation containing both batch and interactive steps.
