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
from dmstudio import dm_io
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
# Tool: read_datamine_file
# ---------------------------------------------------------------------------

@mcp.tool()
def read_datamine_file(filepath: str, max_rows: int = 10) -> str:
    '''
    Read a Datamine binary file (.dm or .dmx) and return a preview.

    Uses DmFile.DmTableADO COM object — requires Datamine Studio RM to be
    installed on this machine. Reads the file without needing an active
    Studio project.

    Args:
        filepath: Full or relative path to the .dm or .dmx file.
        max_rows: Maximum number of rows to include in the preview (default: 10).

    Returns:
        JSON object with 'filepath', 'columns', 'row_count', and 'preview' (list of row dicts).
    '''
    try:
        df = dm_io.read_datamine(filepath)
        preview = df.head(max_rows).to_dict(orient='records')
        return json.dumps({
            'filepath': os.path.abspath(filepath),
            'columns': list(df.columns),
            'row_count': len(df),
            'preview': preview,
        }, indent=2, default=str)
    except Exception as e:
        return json.dumps({'error': str(e)})


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
# Entry point
# ---------------------------------------------------------------------------

def main():
    mcp.run(transport='stdio')

if __name__ == '__main__':
    main()
