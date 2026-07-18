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
      - "type": "markdown" or "code"
      - "content": the cell text or code string

    The notebook is written to disk and can be executed with:
        jupyter nbconvert --to notebook --execute --inplace <notebook_name>

    Args:
        notebook_name: Output filename (e.g. "my_workflow.ipynb"). If the path is
                       relative, it is written to the current working directory.
        steps: List of step dicts. Example:
               [
                 {"type": "markdown", "content": "## Step 1: Initialize"},
                 {"type": "code",     "content": "from dmstudio import dmcommands\\ncmd = dmcommands.init()"},
                 {"type": "markdown", "content": "## Step 2: Sort"},
                 {"type": "code",     "content": "cmd.mgsort(in_i='collars', out_o='sorted', keys_f=['BHID'])"}
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
            step_type = step.get('type', 'code').lower()
            content = step.get('content', '')
            if step_type == 'markdown':
                nb.add_markdown(content)
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


def copy_skills_to_workspace():
    '''Copies package-level skills to the user's workspace so AI agents can index them.'''
    import shutil
    package_dir = os.path.dirname(os.path.abspath(__file__))
    src_skills_dir = os.path.join(package_dir, 'skills')
    dest_skills_dir = os.path.join(os.getcwd(), '.agents', 'skills')

    if not os.path.exists(src_skills_dir):
        return

    try:
        for root, dirs, files in os.walk(src_skills_dir):
            rel_path = os.path.relpath(root, src_skills_dir)
            target_dir = os.path.abspath(os.path.join(dest_skills_dir, rel_path)) if rel_path != '.' else dest_skills_dir
            os.makedirs(target_dir, exist_ok=True)
            for file in files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(target_dir, file)
                shutil.copy2(src_file, dest_file)
        print(f"Successfully copied agent skills to workspace: {dest_skills_dir}")
    except Exception as e:
        print(f"Warning: Failed to copy agent skills to workspace: {e}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Datamine Studio RM MCP Server")
    parser.add_argument("--install", action="store_true", help="Install/register this MCP server on the host machine")
    args = parser.parse_args()

    if args.install:
        success = install_mcp_config()
        copy_skills_to_workspace()
        print("\nConfiguration for other IDEs / AI harnesses (e.g. Cursor, Windsurf, Antigravity, etc.):")
        print("Add a command-type MCP server with the following settings:")
        print(f"  Name: dmstudio")
        print(f"  Command: {sys.executable} -m dmstudio.mcp_server")
        sys.exit(0 if success else 1)
    else:
        mcp.run(transport='stdio')

if __name__ == '__main__':
    main()
