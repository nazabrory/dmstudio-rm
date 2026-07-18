---
name: prepare-env
description: Prepare the dmstudio-rm python environment, install dependencies, and automatically register the MCP server.
---

# Prepare Environment & MCP Server

Use this skill when the user asks to "prepare dmstudio-rm", "set up python environment", "install mcp", or similar environment-setup requests.

## 1. Verify and Install Python dependencies

First, look for a virtual environment in the workspace. Usually, this is in `.venv/` or a conda environment named `dmstudio`.
Run the appropriate setup/install commands to ensure the package and its requirements (including FastMCP) are installed:

- If using the standard `.venv`:
  ```powershell
  .venv\Scripts\pip install -e .
  ```
- If using Conda:
  ```powershell
  conda activate dmstudio
  pip install -e .
  ```

## 2. Install/Configure the MCP Server

Once the package is installed in the active environment, register it as an MCP server.

### For Claude Desktop Users:
Run the automatic installer command:
```powershell
.venv\Scripts\python -m dmstudio.mcp_server --install
```
This automatically updates Claude's `%APPDATA%\Claude\claude_desktop_config.json`.

### For Cursor, Windsurf, and other IDE Users:
Since these editors configure MCP servers via their graphical settings UI rather than a shared configuration file, you must guide the user to add it manually:

1. Retrieve the absolute path of the current python interpreter:
   - Run the command to get the full python executable path.
2. Instruct the user to open their IDE settings:
   - **Cursor**: Go to `Settings` -> `Features` -> `MCP` -> Click `+ Add New MCP Server`.
   - **Windsurf**: Go to `Settings` -> Search for `MCP` -> Click `+ Add New MCP Server`.
3. Provide the user with the exact values to paste into the settings UI:
   - **Name**: `dmstudio`
   - **Type**: `command`
   - **Command**: `<ABSOLUTE_PATH_TO_PYTHON> -m dmstudio.mcp_server` (e.g., `D:\Active\dmstudio-rm\.venv\Scripts\python.exe -m dmstudio.mcp_server`)

Always print these copy-pasteable settings clearly in your final response to guide the user.

---

## CRITICAL: COM Isolation & Workflow Boundaries

To prevent COM session conflicts, project locks, and Datamine Studio RM crashes:

1. **NO Direct COM Access**: The AI agent must never run scripts or commands that directly instantiate Datamine COM processes on the host.
2. **Workflow-Based Design**: The AI's primary role is to act as a workspace assistant that helps the user build and edit Jupyter Notebook workflows (`.ipynb`).
3. **Execution is User-Driven**:
   - Use the `create_jupyter_workflow` MCP tool or programmatically generate notebooks using `NotebookBuilder`.
   - Instruct the user to open and run the notebook cells inside their active Jupyter Lab session (where they have their Studio project safely open).
   - Ask the user to paste any error messages or feedback back into the chat if they need revisions.
