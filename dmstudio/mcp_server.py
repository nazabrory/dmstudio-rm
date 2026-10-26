'''
mcp_server.py
-------------

Datamine Studio RM - Model Context Protocol (MCP) stdio server.

Exposes Datamine capabilities as MCP tools for use with:
  - Claude Desktop
  - Antigravity / Google Gemini
  - Any MCP-compatible AI client

Tools provided:
  - list_commands             : List all available Datamine commands.
  - get_command_schema        : Get full signature and parameters for a command.
  - search_commands           : Fuzzy-search commands by keyword.
  - read_datamine_file        : Load a .dm/.dmx file and return a data preview.
  - create_jupyter_workflow   : Generate an auditable .ipynb notebook from workflow steps.

Usage (standalone):
-------------------
    python -m dmstudio.mcp_server
'''

import json
import sys
import os

# Add project root to path so dmstudio package is importable when run directly
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    raise ImportError(
        'mcp package is required. Install with: pip install "mcp>=1.0.0"'
    )

from dmstudio import command_registry
from dmstudio.notebook_builder import NotebookBuilder
from dmstudio.notebook_runner import run_and_diagnose_notebook as _run_nb
from dmstudio.output_capture import CommandLogCapture

mcp = FastMCP('dmstudio')


# ---------------------------------------------------------------------------
# Tool: list_commands
# ---------------------------------------------------------------------------

@mcp.tool()
def list_commands() -> str:
    '''
    List all available Datamine Studio RM command wrappers.

    Returns a JSON array of objects with 'name' and 'doc' (short description)
    for every command exposed by the dmstudio.dmcommands module.
    '''
    commands = command_registry.list_commands()
    return json.dumps(commands, indent=2)


# ---------------------------------------------------------------------------
# Tool: get_command_schema
# ---------------------------------------------------------------------------

@mcp.tool()
def get_command_schema(command_name: str) -> str:
    '''
    Get the full signature and parameter schema for a Datamine command.

    Args:
        command_name: The Datamine command name (case-insensitive), e.g. "copy" or "MGSORT".

    Returns:
        JSON object with 'name', 'doc', and 'parameters' (list of param dicts).
    '''
    try:
        schema = command_registry.get_command_schema(command_name)
        return json.dumps(schema, indent=2)
    except ValueError as e:
        return json.dumps({'error': str(e)})


# ---------------------------------------------------------------------------
# Tool: search_commands
# ---------------------------------------------------------------------------

@mcp.tool()
def search_commands(query: str) -> str:
    '''
    Search Datamine command names and descriptions for a keyword.

    Args:
        query: Search keyword or phrase (case-insensitive), e.g. "sort", "drillhole", "grade".

    Returns:
        JSON array of matching commands with 'name' and 'doc'.
    '''
    results = command_registry.search_commands(query)
    return json.dumps(results, indent=2)


# ---------------------------------------------------------------------------
# Tool: create_jupyter_workflow
# ---------------------------------------------------------------------------

@mcp.tool()
def create_jupyter_workflow(notebook_name: str, steps: list) -> str:
    '''
    Generate an auditable Jupyter Notebook (.ipynb) from a list of workflow steps.

    Each step is a dict with:
      - "type": "markdown", "code", "command", or "interactive"
      - "content": cell text or code string (for markdown/code steps)
      - "command_name": Datamine command name (for command/interactive steps)
      - "args": dict of keyword parameters (for batch command steps)
      - "instructions": human guidance instructions (for interactive viewport steps)
      - "output_verify_file": filename to verify upon completion (for interactive steps)

    Interactive processes are automatically formatted as Markdown instruction cells
    with 3D viewport guidance accompanied by dataset verification code cells.

    The notebook is written to disk and can be executed with:
        jupyter nbconvert --to notebook --execute --inplace <notebook_name>

    Args:
        notebook_name: Output filename (e.g. "my_workflow.ipynb"). If the path is
                       relative, it is written to the current working directory.
        steps: List of step dicts. Example:
               [
                 {"type": "markdown", "content": "## Step 1: Initialize"},
                 {"type": "code",     "content": "from dmstudio import dmcommands\\ncmd = dmcommands.init()"},
                 {"type": "command",  "command_name": "copy", "args": {"in_i": "collars", "out_o": "sorted"}},
                 {"type": "command",  "command_name": "intext", "instructions": "Select text file in dialog", "output_verify_file": "imported_pts"}
               ]

    Returns:
        JSON object with 'notebook_path' and 'cell_count'.
    '''
    try:
        if not notebook_name.endswith('.ipynb'):
            notebook_name += '.ipynb'

        # Derive a title from the filename
        title = os.path.splitext(os.path.basename(notebook_name))[0].replace('_', ' ').title()

        nb = NotebookBuilder(notebook_name, title=title)

        for step in steps:
            step_type = step.get('type', '').lower()
            cmd_name = step.get('command_name') or step.get('command')
            content = step.get('content', '')

            if step_type == 'markdown':
                nb.add_markdown(content)
            elif cmd_name:
                nb.add_command_step(
                    command_name=cmd_name,
                    args=step.get('args'),
                    instructions=step.get('instructions'),
                    output_verify_file=step.get('output_verify_file'),
                    is_interactive=(step_type == 'interactive')
                )
            else:
                nb.add_code(content)

        path = nb.save()
        return json.dumps({
            'notebook_path': path,
            'cell_count': len(nb._cells),
            'execute_command': 'jupyter nbconvert --to notebook --execute --inplace "{}"'.format(path),
        }, indent=2)
    except Exception as e:
        return json.dumps({'error': str(e)})


# ---------------------------------------------------------------------------
# Tool: run_and_diagnose_notebook
# ---------------------------------------------------------------------------

@mcp.tool()
def run_and_diagnose_notebook(notebook_path: str, timeout: int = 120, sandbox_dir: str = '') -> str:
    '''
    Execute a Jupyter Notebook headlessly against the active Datamine Studio RM session,
    monitoring each cell's Python traceback and pairing it with real-time Command.log output.

    If any cell fails (due to a Python exception or Datamine syntax/field error), execution
    halts and returns a Cell-Paired Diagnostic Bundle detailing the exact failing cell,
    code, error type, and Datamine Command Window output delta.

    Args:
        notebook_path: Path to the .ipynb file.
        timeout: Maximum execution timeout in seconds (default 120).
        sandbox_dir: Optional sandbox working directory (e.g. "tutorials/test_sandbox").

    Returns:
        JSON object with 'success', 'total_cells', 'failed_cell_index', 'failed_cell_code',
        'error_type', 'error_message', 'command_log_delta', and 'summary'.
    '''
    sbox = sandbox_dir if sandbox_dir.strip() else None
    report = _run_nb(notebook_path=notebook_path, timeout=timeout, sandbox_dir=sbox)
    return json.dumps(report, indent=2)


# ---------------------------------------------------------------------------
# Tool: read_recent_command_log
# ---------------------------------------------------------------------------

@mcp.tool()
def read_recent_command_log(lines: int = 50) -> str:
    '''
    Read the most recent lines from Datamine Studio RM's native Command.log file
    located in %APPDATA%/Datamine/StudioRM/Command.log.

    Allows the AI agent to inspect recent Datamine CLI diagnostic messages and
    execution output without attaching to COM.

    Args:
        lines: Number of trailing log lines to retrieve (default 50).

    Returns:
        JSON object with 'log_path', 'line_count', and 'content'.
    '''
    log_path = CommandLogCapture.default_log_path()
    if not os.path.exists(log_path):
        return json.dumps({
            'error': f'Command.log not found at {log_path}',
            'log_path': log_path,
        }, indent=2)

    try:
        with open(log_path, 'r', encoding='utf-8', errors='replace') as f:
            all_lines = f.readlines()
        tail = all_lines[-lines:] if len(all_lines) > lines else all_lines
        return json.dumps({
            'log_path': log_path,
            'line_count': len(tail),
            'content': ''.join(tail),
        }, indent=2)
    except Exception as e:
        return json.dumps({'error': str(e), 'log_path': log_path}, indent=2)


# ---------------------------------------------------------------------------
# MCP Resource: agent-rules
# ---------------------------------------------------------------------------

@mcp.resource(
    uri="resource://dmstudio/agent-rules",
    name="Datamine Studio RM AI Agent Rules",
    description="Guidelines, constraints, and standard workflows for AI agents scripting Datamine Studio RM via dmstudio."
)
def get_agent_rules() -> str:
    '''
    Retrieve the Datamine Studio RM AI Agent Rules markdown document.
    '''
    package_dir = os.path.dirname(os.path.abspath(__file__))
    rules_path = os.path.join(package_dir, 'agent_rules.md')
    if not os.path.exists(rules_path):
        return "# Error\nAgent rules file not found inside the package distribution."
    
    with open(rules_path, 'r', encoding='utf-8') as f:
        return f.read()


# ---------------------------------------------------------------------------
# MCP Prompt: dmstudio-rules
# ---------------------------------------------------------------------------

@mcp.prompt(
    name="dmstudio-rules",
    title="Datamine Studio RM AI Rules",
    description="Inject the critical guidelines and constraints for writing Datamine Studio RM COM scripts into the agent's context."
)
def dmstudio_rules() -> list:
    '''
    Provide the agent rules and constraints as a developer message.
    '''
    content = get_agent_rules()
    return [
        {
            "role": "user",
            "content": "Please review and adhere to the following rules when working with the dmstudio library:\n\n{}".format(content)
        }
    ]


# ---------------------------------------------------------------------------
# Installer & Entry point
# ---------------------------------------------------------------------------


def install_mcp_config():
    '''Registers the MCP server in Claude Desktop config and prints setup info.'''
    appdata = os.environ.get('APPDATA')
    if not appdata:
        print("Error: APPDATA environment variable not found. Cannot auto-install Claude Desktop config.")
        return False

    config_dir = os.path.join(appdata, 'Claude')
    config_path = os.path.join(config_dir, 'claude_desktop_config.json')

    # Ensure config directory exists
    os.makedirs(config_dir, exist_ok=True)

    # Load existing or initialize new config
    config = {}
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
        except Exception as e:
            print(f"Warning: Failed to parse existing Claude Desktop config: {e}. Starting fresh.")

    if 'mcpServers' not in config:
        config['mcpServers'] = {}

    # Register the server with the absolute path of the current python interpreter
    config['mcpServers']['dmstudio'] = {
        'command': sys.executable,
        'args': ['-m', 'dmstudio.mcp_server']
    }

    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        print(f"Successfully auto-configured Claude Desktop!")
        print(f"Config file updated: {config_path}")
    except Exception as e:
        print(f"Error writing to Claude Desktop config file: {e}")
        return False
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Datamine Studio RM MCP Server")
    parser.add_argument("--install", action="store_true", help="Install/register this MCP server on the host machine")
    parser.add_argument("--install-skills", action="store_true", help="Install AI agent skill markdown files into the current workspace (.agents/skills/)")
    args = parser.parse_args()

    if args.install_skills:
        from dmstudio.bootstrap import install_agent_skills
        try:
            install_agent_skills()
            sys.exit(0)
        except Exception as e:
            print("Error: {}".format(e))
            sys.exit(1)
    elif args.install:
        success = install_mcp_config()
        print("\nConfiguration for other IDEs / AI harnesses (e.g. Cursor, Windsurf, Antigravity, etc.):")
        print("Add a command-type MCP server with the following settings:")
        print("  Name: dmstudio")
        print("  Command: {} -m dmstudio.mcp_server".format(sys.executable))
        sys.exit(0 if success else 1)
    else:
        mcp.run(transport='stdio')

if __name__ == '__main__':
    main()
