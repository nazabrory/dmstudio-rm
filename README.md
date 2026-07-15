DMSTUDIO
========

Python package for Datamine Studio RM scripting via Windows COM automation.

The package provides an easy-to-use interface between Python and Datamine Studio packages for creating concise, highly readable, and powerful Datamine scripts. It is designed for people familiar with Datamine commands and scripting, and also provides a relatively easy entry point for those learning Datamine scripting.

The ``dmstudio`` package requires an active Datamine Studio project and therefore requires a valid Datamine license to be of any use. Visit the [Datamine Software](http://www.dataminesoftware.com) website for more information on products, licenses and downloads.

The python code was auto-generated from the ``StudioRM.chm`` help file. Scripts created using the ``dmstudio`` package can be executed in a number of ways including the command line, IDEs such as [Pycharm](https://www.jetbrains.com/pycharm/), [Jupyter Notebook](http://jupyter.org/), and just about any way you can think of.

Versions supported are:

* Datamine Studio version 3
* Datamine Studio version RM
* Datamine Studio version RM 3.1
* Datamine Studio version EM

What's New (v2.0-beta)
----------------------

* **AI Agent Support** - New `dmstudio.agent` module providing `list_commands()`, `get_command_schema()`, `search_commands()`, `read_datamine()`, and `dialog_dismiss_context()` for autonomous AI workflows.
* **MCP Server** - Expose Datamine capabilities via `mcp_server.py` as a Model Context Protocol stdio server for use with Claude Desktop, Antigravity, and other MCP-compatible clients.
* **Jupyter Notebook Builder** - New `dmstudio.notebook_builder.NotebookBuilder` class for programmatically generating auditable `.ipynb` workflow notebooks.
* **Native Datamine File Reader** - `read_datamine()` in `dmstudio.agent` uses `DmFile.DmTableADO` COM object to read `.dm`/`.dmx` binary files directly into pandas DataFrames — no proprietary dependencies required.
* **Studio RM 3.3+ Compatibility** - `initialize.studio()` now dynamically resolves any `StudioRM3.x` version string, future-proofing compatibility.
* Added ``copymod`` command (supports retrieval criteria in 3.1)
* Added ``update_scripts`` command for batch script conversion to safer syntax
* Updated ``compdh`` with up to 5 ZONE fields and 5 DOM fields (3.1 enhancement)
* Updated ``modsplit`` to allow optional ``modelout`` and/or ``fullmod`` outputs (3.1 enhancement)
* Added ``print_plot_sheet_to_pdf`` automation helper for PDF output via COM
* Fixed ``dmfiles.comres`` zone field reference bug
* Fixed deprecated ``pandas.DataFrame.append()`` usage for pandas 2.0+ compatibility
* Fixed deprecated ``numpy.str.split`` usage for numpy 1.20+ compatibility

The package is made up of the following modules:

* ``dmcommands`` - a complete set of Studio commands that require input files as they appear in the StudioRM.chm help file.
* ``dmfiles`` - the remaining Studio commands that do not use input files and are mainly used for generating Datamine files.
* ``special`` - some special functions which are adaptations of Studio commands.
* ``superprocess`` - special functions that involve a chain of Studio commands.
* ``agent`` - AI agent helpers for command discovery, file reading, and dialog management.
* ``notebook_builder`` - Jupyter Notebook builder for auditable AI agent workflows.

License
-------

Original work copyright (c) 2018 Sean D. Horan — released under [MIT License](LICENSE.txt).

Modifications and new contributions (AI agent module, MCP server, Notebook Builder, Studio RM 3.3+ support) copyright (c) 2025 nazabrory contributors.

The MIT license permits modification and redistribution provided the original copyright notice is preserved. See [LICENSE.txt](LICENSE.txt) for full terms.

Datamine Commands
-----------------

An exhaustive set of Datamine Studio commands is available in the ``dmstudio.dmcommands`` and the ``dmstudio.dmfiles`` modules. The variables consist of four parts:

* Input files
* Output files
* Fields
* Parameters

The python input variables are identical to the variable names used by Datamine with the following exceptions:

* All variables are lowercase
* Input files have the suffix ``_i``, output files have the suffix ``_o``, fields have the suffix ``_f`` and parameters have the suffix ``_p``.
* Multiple field selection is entered as a list instead of multiple variables for some commands e.g f1, f2, f3 => fields=[f1, f2, f3]

The ``dmstudio.dmfiles`` module is for commands such as ``INPFIL`` which requires an output file and a string of arguments. The purpose of the ``dmstudio.special`` module is to simplify the usage of some processes such as ``dmstudio.dmfiles.inpfil``.

Default values are used when they were specified by the StudioRM.chm help file. In order to provide guidance as to required versus optional inputs, outputs fields and parameters, python variables without a default specified but which are required are given a default string ``"required"`` while those which are optional are given the default ``"optional"``. This is particularly useful when using IDEs which have code completion.

AI Agent Capabilities
---------------------

The ``dmstudio.agent`` module exposes tools for AI agents to introspect and execute Datamine workflows:

```python
from dmstudio import agent

# Discover commands
commands = agent.list_commands()
schema = agent.get_command_schema('COPY')
results = agent.search_commands('sort')

# Read Datamine files natively (no proprietary deps)
df = agent.read_datamine('myfile.dmx')

# Auto-dismiss blocking modal dialogs (opt-in)
with agent.dialog_dismiss_context():
    cmd.copy(in_i='source', out_o='dest')
```

MCP Server
----------

Run the MCP stdio server to expose Datamine capabilities to Claude Desktop, Antigravity, or any MCP client:

```bash
# Run standalone
.venv\Scripts\python mcp_server.py

# Claude Desktop config (~\AppData\Roaming\Claude\claude_desktop_config.json):
{
  "mcpServers": {
    "dmstudio": {
      "command": "C:\\path\\to\\project\\.venv\\Scripts\\python",
      "args": ["C:\\path\\to\\project\\mcp_server.py"]
    }
  }
}
```

MCP tools available:
- ``list_commands`` - List all Datamine commands
- ``get_command_schema(command_name)`` - Get full command signature
- ``read_datamine_file(filepath)`` - Preview a `.dm`/`.dmx` file as JSON
- ``create_jupyter_workflow(notebook_name, steps)`` - Build an auditable Jupyter Notebook

Jupyter Notebook Builder
------------------------

Generate auditable workflows as Jupyter Notebooks instead of running commands directly:

```python
from dmstudio.notebook_builder import NotebookBuilder

nb = NotebookBuilder('my_workflow.ipynb', title='Drillhole De-Survey Workflow')
nb.add_markdown('## Step 1: Initialize')
nb.add_code("from dmstudio import dmcommands\ncmd = dmcommands.init(version='StudioRM')")
nb.add_markdown('## Step 2: Sort')
nb.add_code("cmd.mgsort(in_i='collars', out_o='sorted_collars', keys_f=['BHID'])")
nb.save()
# Execute: jupyter nbconvert --to notebook --execute --inplace my_workflow.ipynb
```

Usage
-----

Using the ``dmstudio.dmcommands`` module:

    >>> from dmstudio import dmcommands
    >>> cmd = dmcommands.init(version='StudioRM')
    >>> cmd.copy(in_i='fake_model', out_o='fake_model_copy', retrieval='AU>2.0')

Using the ``dmstudio.dmfiles`` module:

    >>> from dmstudio import dmfiles
    >>> dmf = dmfiles.init(version='StudioRM')
    >>> arguments = "'XXXXXXXX'"
    >>> dmf.infile(out_o='points', arguments=arguments)

Initialization
--------------

The COM object is initialized using ``win32com.client`` package and is passed to a variable ``oScript`` which is consistent with traditional Datamine Studio javascripts or ``vbscript``. Each module is required to be initialized separately although in reality they are redundantly initializing the same COM object. There is only a minor impact on processing time which is noticeable only when running scripts on small data sets.

Installation
------------

### Prerequisites

- **Windows OS** (required for COM automation with Datamine Studio)
- **Python 3.9 or later** - Download from [python.org](https://www.python.org/downloads/)
- **Active Datamine Studio license** (required at runtime)

### Quick Start (Recommended)

The easiest way to set up the environment is using the provided setup scripts:

**Option 1: Using Command Prompt**
```batch
setup_env.bat
```

**Option 2: Using PowerShell**
```powershell
.\setup_env.ps1
```

These scripts will:
1. Create a Python virtual environment (``.venv``)
2. Install all dependencies from ``requirements.txt``
3. Install dmstudio in development mode

### Manual Installation

If you prefer to set up manually:

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows Command Prompt)
.venv\Scripts\activate.bat

# Activate (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Install dmstudio in development mode
pip install -e .
```

### Anaconda/Conda Alternative

For Anaconda users:

```bash
conda create -n dmstudio python=3.10
conda activate dmstudio
pip install -r requirements.txt
pip install -e .
```

### Verify Installation

```python
python -c "from dmstudio import dmcommands; print('dmstudio installed successfully')"
```

Examples
--------

See the ``examples/`` folder for sample scripts and tutorials:

* ``studio_rm_31_example.py`` - Python script demonstrating Studio RM 3.1 features
* ``Holes3D_Tutorial.ipynb`` - Interactive Jupyter notebook tutorial demonstrating the Holes3D scripting workflow (sort, merge, join, de-survey)
