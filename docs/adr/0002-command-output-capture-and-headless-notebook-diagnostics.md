# ADR-0002: Command Output Capture and Autonomous Headless Notebook Diagnostics

## Status

Accepted

## Context

Automating Datamine Studio RM via Python scripts and AI agents presents two fundamental challenges:
1. **Write-Only COM Output**: The native Datamine COM automation interface (`IDmOutputControlBar` accessed via `oDmApp.ControlBars.Command` and `oDmApp.ControlBars.Output`) provides only write methods (`Write`, `WriteLine`, `Clear`, `SetTextColour`). It exposes no method or property to read back text emitted by Datamine processes.
2. **COM Isolation & Process Deadlocks**: The `dmstudio-mcp` server adheres to a strict COM isolation policy to prevent application deadlocks and stdio stream freezes caused by blocking Windows modal dialogs or long-running computations. Consequently, the AI agent cannot attach directly to the COM session within the server process.

At the same time, Datamine processes frequently fail silently from a COM perspective (returning `void` from `Parsecommand()`) while printing critical syntax errors, missing field notices, or sorting requirements exclusively to the GUI Command Window. Without access to these messages, AI agents cannot autonomously diagnose errors or refine generated notebooks.

## Decision

We have decided to establish a two-tier architecture for output capture and autonomous notebook diagnostics:

1. **Session Log Delta via `Command.log`**:
   - Rather than relying on fragile Win32 GUI control scraping, `dmstudio` taps into Studio RM's native streaming log file located at `%APPDATA%\Datamine\StudioRM\Command.log`.
   - Before executing a command, the system records the current byte seek position of `Command.log`.
   - After `Parsecommand()` finishes, the newly appended slice (**Session log delta**) is read and parsed.
   - Known Datamine error signatures (`>>> ERROR`, `Fatal:`, `Invalid field`, `does not exist`) and completion tokens (`>>> <PROCESS> Complete <<<`) are matched to determine success or failure deterministically.

2. **Headless Notebook Execution Loop (`run_and_diagnose_notebook`)**:
   - The MCP server remains decoupled from COM.
   - An MCP tool `run_and_diagnose_notebook(notebook_path, timeout=120)` is introduced. It spawns a dedicated, short-lived subprocess executing the target notebook headlessly in `tutorials/test_sandbox/`.
   - The execution is wrapped in `dmstudio.dialog.dialog_dismiss_context` to prevent hangs from unexpected modal prompts, with a hard process timeout.

3. **Cell-Paired Diagnostic Bundle**:
   - When a notebook cell fails during headless execution, the runner extracts:
     - The cell index and failing Python code.
     - The standard Python traceback/exception.
     - The exact slice of `Command.log` generated during that specific cell's execution.
   - This bundle is returned to the AI agent, allowing it to autonomously patch and re-run the notebook until fully verified.

4. **Package-Level Dual Mode (`dmcommands`)**:
   - In `dmstudio.dmcommands`, `run_command` returns an `ExecutionResult` object containing `.success`, `.output`, and `.duration`.
   - A context manager `command_capture()` is provided for block-level workflow logging in standalone scripts.

## Consequences

- **Stability**: The MCP server never touches COM directly; unexpected modal dialogs or Datamine crashes cannot hang the AI communication channel.
- **Autonomy**: AI agents gain a complete closed-loop feedback mechanism: generate notebook $\rightarrow$ execute headlessly $\rightarrow$ inspect cell-level diagnostics $\rightarrow$ revise script.
- **Auditability**: End users receive clean, fully executed, and reproducible `.ipynb` notebooks with rich outputs, while maintaining complete diagnostic transparency.
