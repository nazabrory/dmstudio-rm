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
Run the server's built-in installer:

```powershell
.venv\Scripts\python -m dmstudio.mcp_server --install
```

This command will:
1. Locate the absolute path of the python interpreter for the active environment.
2. Automatically update/configure Claude Desktop's `%APPDATA%\Claude\claude_desktop_config.json` to register the `dmstudio` MCP server.
3. Automatically copy this and other workspace agent skills into the local `.agents/skills/` directory so they are indexed by your IDE/AI.
4. Print copy-pasteable configuration details (Name, Command) for other IDEs (e.g., Cursor, Windsurf, Antigravity, etc.).

Present these printed copy-pasteable configuration details clearly to the user in your final response so they can easily register it in their respective AI tool if they aren't using Claude Desktop.

---

## CRITICAL: COM Isolation & Workflow Boundaries

To prevent COM session conflicts, project locks, and Datamine Studio RM crashes:

1. **NO Direct COM Access**: The AI agent must never run scripts or commands that directly instantiate Datamine COM processes on the host.
2. **Workflow-Based Design**: The AI's primary role is to act as a workspace assistant that helps the user build and edit Jupyter Notebook workflows (`.ipynb`).
3. **Execution is User-Driven**:
   - Use the `create_jupyter_workflow` MCP tool or programmatically generate notebooks using `NotebookBuilder`.
   - Instruct the user to open and run the notebook cells inside their active Jupyter Lab session (where they have their Studio project safely open).
   - Ask the user to paste any error messages or feedback back into the chat if they need revisions.
