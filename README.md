# dmstudio-rm: Python wrappers for Datamine Studio RM with AI capabilities

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python Version"></a>
  <a href="https://img.shields.io/badge/version-2.0.0b9-purple.svg" alt="Version"></a>
  <a href="LICENSE.txt"><img src="https://img.shields.io/badge/license-GPL--3.0-blue.svg" alt="License"></a>
  <a href="https://www.dataminesoftware.com/"><img src="https://img.shields.io/badge/Datamine-Studio%20RM-orange.svg" alt="Datamine Studio RM"></a>
</p>

**dmstudio** is a user-friendly Python package designed for geologists and engineers to automate **Datamine Studio RM** workflows. It translates complex Datamine macro syntax into readable, interactive Python commands. The entire workflow is designed to run in interactive **JupyterLab** (or Jupyter Notebooks), where you can run processes and analyze results step-by-step.

> **Unofficial Disclaimer & Licensing**  
> This is a community-maintained library and is **NOT** an official product of Datamine Software. Datamine Software does not provide support or warranties for this package.
>
> This library uses official Datamine COM Automation APIs (`Datamine.StudioRM.Application` and `DmFile.DmTableADO`) which are built into Studio RM. To run the automation, you **must already own a valid, licensed instance** of Datamine Studio RM running on your system. This library does not bypass or clone any Datamine proprietary code.

For deep developer and AI-agent guidance (full module map, COM engineering rules, generators, code style), see **[AGENTS.md](AGENTS.md)**.

---

## 🏗️ Architecture & How It Works

`dmstudio` acts as a Pythonic bridge to the desktop instance of Datamine Studio RM using Windows COM automation APIs. Command wrappers build Studio CLI strings and dispatch them through `Parsecommand`; table I/O can also go directly through the ADO file reader without exporting via a process.

```mermaid
flowchart TD
    %% Styling and colors
    classDef user fill:#1a252f,stroke:#2c3e50,stroke-width:2px,color:#ffffff;
    classDef dm fill:#16a085,stroke:#1abc9c,stroke-width:2px,color:#ffffff;
    classDef com fill:#2980b9,stroke:#3498db,stroke-width:2px,color:#ffffff;
    classDef rm fill:#d35400,stroke:#e67e22,stroke-width:2px,color:#ffffff;

    subgraph UserSpace ["User Space (JupyterLab / Python Environment)"]
        A["Jupyter Notebook (.ipynb) or Script"]:::user
        B["Import dmstudio & initialize"]:::user
    end

    subgraph DmStudio ["dmstudio Package (Python Wrapper)"]
        C["dmcommands / dmfiles<br/>(Command wrappers)"]:::dm
        D["dm_io<br/>(DataFrame ↔ .dm / .dmx)"]:::dm
        E["dialog.dialog_dismiss_context()<br/>(Optional background thread)"]:::dm
    end

    subgraph COMLayer ["Windows COM Automation Layer"]
        F["Datamine.StudioRM.Application<br/>(COM Object Interface)"]:::com
        G["DmFile.DmTableADO<br/>(Fast Direct File ADO Reader)"]:::com
    end

    subgraph StudioRM ["Datamine Studio RM (Desktop App)"]
        H["Active Project (.rmproj)<br/>(Loaded in memory)"]:::rm
        I["Execute CLI Commands<br/>(Parsecommand / run_command)"]:::rm
        J["Dismiss Blocking Modal Dialogs<br/>(Win32 GUI Events)"]:::rm
        K[("Datamine Binary Files<br/>(.dm / .dmx on disk)")]:::rm
    end

    %% Relationships
    A -->|1. Imports & Configures| B
    B -->|2. Calls wrapper function| C
    C -->|3. Connects to COM interface| F
    B -->|4. Optional dialog monitor| E
    F -->|5. Dispatches script parser| I
    I -->|6. Manipulates active workspace| H
    E -->|Monitoring thread| J
    J -->|Closes #32770 popups| I
    B -->|Direct table I/O| D
    D --> G
    G -->|Direct binary read/write| K
    I -->|Reads/Writes data| K
```

---

## 📖 User Guide

This section is for geologists and engineers who want to install, run, and automate workflows in Datamine using Python.

### 📋 Prerequisites & Environment Preference

Before setting up `dmstudio`, please ensure your computer has the following:

1. **Windows OS**: Datamine Studio RM runs exclusively on Windows.
2. **Datamine Studio RM**: Installed and licensed on your machine.
3. **Python Environment (Anaconda/Miniconda Preferred)**:
   * **Preference**: We highly recommend installing **Anaconda** or **Miniconda** (from [docs.conda.io](https://docs.conda.io/en/latest/miniconda.html)) as it simplifies managing virtual environments and package installations for geological data analysis.
   * **Alternative (Vanilla Python)**: Download the installer from [Python.org](https://www.python.org/downloads/windows/). **IMPORTANT**: During installation, check the box that says **"Add Python to PATH"** (usually at the bottom of the installer window).
   * **Also supported**: [uv](https://github.com/astral-sh/uv) for a fast virtual environment workflow.

Open your Datamine project (e.g. `MyProject.rmproj`) in Studio RM before running any script that uses COM automation.

---

### 🛠️ Installation

#### 📦 Option A: Install from PyPI (Recommended)
The easiest way to install `dmstudio-rm` is directly from PyPI. Open your terminal or command prompt and run:
```bash
pip install dmstudio-rm
```

#### 🔧 Option B: Local Source Installation (For Contributors & Tutorials)
If you want to customize the wrappers, run the full test suite, or access the built-in Jupyter notebook tutorials locally, clone or download this repository (e.g. into `C:\path\to\dmstudio-rm`) and choose one of the options below:

##### Conda (Recommended)
Use the provided `environment.yml` to create a dedicated conda environment and install the cloned source in editable mode:
```cmd
# Open Anaconda Prompt / Terminal and navigate to the repo folder
cd C:\path\to\dmstudio-rm

# Create the environment
conda env create -f environment.yml

# Activate the environment
conda activate dmstudio

# Install the dmstudio package in editable mode
pip install -e .
```

##### Using uv
Create and install dependencies instantly using [uv](https://github.com/astral-sh/uv):
```cmd
cd C:\path\to\dmstudio-rm
uv venv
.venv\Scripts\activate

# Install dependencies and the package
uv pip install -r requirements.txt
uv pip install -e .
uv pip install jupyterlab
```

##### One-Click Windows Setup (Vanilla Python)

If you are using vanilla Python:

1. Open **Datamine Studio RM** and load your active project file (e.g. `MyProject.rmproj`).
2. Open the repository folder `C:\path\to\dmstudio-rm`.
3. Double-click **`setup_env.bat`**. This creates a virtual environment (`.venv`), installs required libraries (including Pandas and JupyterLab), and links `dmstudio` in editable mode. PowerShell alternative: `.\setup_env.ps1`.
4. Double-click **`start_jupyter.bat`** to launch JupyterLab in your browser. Keep the command prompt window open while you work.

---

### ⚠️ Directory Alignment: Connecting Python & Datamine

> [!IMPORTANT]
> **Working Directory Mismatch**  
> Datamine commands execute relative to your **active Datamine project folder**, but Python runs code relative to the directory where your **Jupyter Notebook file** is opened.
>
> If you start JupyterLab directly in the repository root while your data lives elsewhere, Python will be unable to read or write files generated by Datamine in your project directory.

#### Best Practice for Aligning Directories

Always open or create your Jupyter Notebooks **inside your Datamine project folder** (e.g. `C:\path\to\MyMineProject`).

Since `dmstudio` is installed in editable/development mode, it is available in your environment from any working directory. You can start JupyterLab from your project folder as follows:

1. Create a script named `start_project.bat` in your **Datamine Project Folder**.
2. Add these lines (pointing at the environment in your repository folder):
   ```bat
   @echo off
   call C:\path\to\dmstudio-rm\.venv\Scripts\activate.bat
   jupyter lab
   ```
   *(For Conda, replace the activate call with `call conda activate dmstudio`.)*
3. Double-click `start_project.bat` to launch JupyterLab inside your project directory. All Python code and Datamine actions will then share the same working folder.

---

### 🚀 Running the Included Tutorials

The repository comes with pre-packaged tutorial data and workflows.

> [!NOTE]
> **Automatic Directory Alignment**  
> Unlike custom user scripts, the included tutorial notebooks automatically align Python's working directory to the active Datamine sandbox folder using `initialize_sandbox()`. You do not need to create or run any manual directory alignment scripts to use them.

#### Option A: Running from a Local Git Repository

1. In Datamine Studio RM, open the tutorial project **`tutorials\test_sandbox\Project.rmproj`** under your clone (e.g. `C:\path\to\dmstudio-rm\tutorials\test_sandbox\Project.rmproj`).
2. Start JupyterLab from the repository root (`start_jupyter.bat`) or from the folder of the notebook you intend to run.
3. In the JupyterLab sidebar:
   * **Workflows and Case Studies (`tutorials/workflows/`)**: Multi-command workflow tutorials and end-to-end case studies. Start with `holes3d_desurvey/Holes3D_Tutorial.ipynb` for de-surveying, or `grade_estimation/Grade_Estimation_Examples.ipynb` for block modeling. Advanced examples live in `studio_rm_examples/`, and AI agent workflows live in `ai_agent_workflow_tutorial.ipynb`.
   * **Process Collections (`tutorials/collections/`)**: Reference notebooks for individual commands, including both auto-generated process/file wrappers and hand-tuned examples (like `cokrig_example.ipynb`, `estima_example.ipynb`, and `protom_example.ipynb`).

#### Option B: Downloading Tutorials Dynamically (For pip/conda Installs)

If you installed `dmstudio` without cloning this repository, you can download the tutorials folder into your workspace:

```python
import dmstudio

# Download and extract the tutorials folder (implemented in dmstudio.bootstrap)
dmstudio.download_tutorials(r'C:\path\to\workspace')
```

This downloads and extracts the tutorials workspace structure. Open Datamine Studio RM, load the downloaded `tutorials/test_sandbox/Project.rmproj`, and start JupyterLab in that directory.

---

### 💡 Basic Scripting Example

Here is a typical automation script inside a Jupyter Notebook:

```python
from dmstudio import dmcommands

# 1. Connect to your open Studio RM session (automatically detects version)
cmd = dmcommands.init()

# 2. Sort drillhole assays by Hole ID (BHID) and Depth (FROM)
cmd.mgsort(in_i='assays', out_o='sorted_assays', keys_f=['BHID', 'FROM'])

# 3. Filter for samples with gold grade (AU) greater than 1.5
cmd.copy(in_i='sorted_assays', out_o='high_grade_assays', retrieval='AU > 1.5')
```

#### Two-Tier Command Wrapper Architecture

To guarantee script stability and prevent blocking UI modals, `dmstudio` separates command wrappers into two distinct namespaces:
* **Verified Core (`from dmstudio import dmcommands, dmfiles`)**: Contains the 23 verified core commands (e.g., `mgsort`, `copy`, `inpfil`, `stats`, `join`) tested in sandbox environments to execute reliably without manual UI interactivity.
* **Experimental/Generated (`from dmstudio import dmcommands_generated, dmfiles_generated`)**: Exposes the remaining 280+ auto-generated wrappers. These are unverified, untested, and may trigger blocking interactive modal dialogs.

#### Suffix Naming Convention Guide

To translate Datamine's command arguments into Python parameters:

| Suffix | Meaning | Example |
|--------|---------|---------|
| `_i` | **Input File** | `in_i='assays'` |
| `_o` | **Output File** | `out_o='sorted_assays'` |
| `_f` | **Field Name** | `keys_f=['BHID']` |
| `_p` | **Parameter Value** | `allrecs_p=1` |

---

### 🔍 Advanced Python Utility Modules

Beyond running standard processes, `dmstudio` provides helper tools for high-speed data analysis and safer automation.

**Prefer the canonical modules below.** Older notebooks may still use `from dmstudio import agent` — that module **re-exports** the same helpers for backward compatibility and is not the implementation home.

#### Direct File Reading into Pandas DataFrames

Instead of running a Datamine command to export files, you can read Datamine binary tables (`.dm` / `.dmx`) directly into a Pandas DataFrame using the ADO COM interface:

```python
from dmstudio import dm_io

# Read Datamine file directly into a pandas DataFrame
df = dm_io.read_datamine('high_grade_assays.dm')

# Perform standard pandas data analysis
print(df.head())
print(df['AU'].describe())

# Write a DataFrame back when needed
dm_io.to_datamine(df, 'from_pandas.dm')
```

#### Handling Blocking Dialog Modals

Datamine runs script commands on its main thread. If a command prompts a modal dialog (warning, overwrite, or error popup), the script can hang indefinitely. Wrap risky sequences in the dialog dismisser:

```python
from dmstudio import dmcommands, dialog

cmd = dmcommands.init()

with dialog.dialog_dismiss_context():
    # Warning dialogs are auto-closed in the background
    cmd.copy(in_i='nonexistent', out_o='temp')
```

Command discovery for AI tools and scripts (`list_commands`, `get_command_schema`, `search_commands`) lives in `dmstudio.command_registry`. See [AGENTS.md](AGENTS.md) for the full package surface.

---

### ⚠️ Important Scripting Rules & Pitfalls

Datamine COM scripting has specific rules. Keep these in mind to avoid common errors:

1. **No Backslashes or Spaces in Command Paths**  
   Datamine's internal parser splits strings by spaces and treats backslashes abnormally. Passing a path like `in_i="C:\My Data\file"` will crash the parser.
   * *Best Practice*: Work entirely within your project folder and use simple filenames (`in_i="assays"`).
   * *Solution*: Register the file in Datamine first using the logical path mechanism:
     ```python
     # Add external file to Datamine workspace
     cmd.oScript.ActiveProject.AddFile(r'C:\My Data\file.dm')

     # Now call the command using the registered file name (no path)
     cmd.mgsort(in_i='file', out_o='sorted')
     ```

2. **In-Memory Scratch Files**  
   Files with a leading underscore (e.g. `_sorted`) are kept by Datamine in RAM and are **never** written to disk. Use them for temporary steps. If you need to verify output files on disk, use normal names without a leading underscore.

3. **Handling Blocking Dialog Modals**  
   Use `dialog.dialog_dismiss_context()` as shown above (also available as `agent.dialog_dismiss_context` for older scripts). Full COM checklist: [AGENTS.md](AGENTS.md).

---

### 🤖 AI Integration Capabilities

#### Model Context Protocol (MCP) Server Setup
To expose Datamine automation tools to your AI agent, configure it as an MCP server:

##### Option A: Claude Desktop (Automated Setup)
1. Ensure `dmstudio-rm` is installed in your active Python environment.
2. Run the automatic installer:
   ```cmd
   python -m dmstudio.mcp_server --install
   ```
   This automatically detects the environment's python path and writes/merges the settings to Claude's `%APPDATA%\Claude\claude_desktop_config.json`.
3. Restart Claude Desktop.

##### Option B: Cursor, Windsurf, and other IDEs (AI-Assisted Setup)
Since these IDEs configure MCP servers via their graphical user interface rather than a shared configuration file, you can utilize your editor's AI assistant to help you locate and generate the exact paths for registration:

1. **Ask your IDE's AI assistant** how custom MCP servers are registered in this editor:
   > *"How do I register a custom command-type MCP server in this editor/client?"*

2. Once the AI explains where the settings are (e.g. Cursor's Settings UI or Windsurf's settings JSON), **copy-paste the following follow-up prompt** into the chat window:
   ```text
   I have installed `dmstudio-rm` in my python virtual environment. Please run a quick python check to find the absolute path of my environment's python interpreter and the installed `dmstudio` package (e.g. searching for `.venv`, `venv`, `.conda`, or using `python -c "import sys; print(sys.executable)"`).

   Once you have the path, please:
   1. Guide me step-by-step to the settings page in this editor.
   2. Print the exact Name, Type (command), and Command string (using the absolute path to python/module, e.g. `C:\path\to\.venv\Scripts\python.exe -m dmstudio.mcp_server`) so I can copy-paste it directly into the settings pane.
   ```
3. Copy the path generated by the AI and paste it into the editor's MCP settings pane. Save and restart your chat session.

#### COM Isolation & Security
To prevent project locking and Datamine application crashes, the AI assistant operates under strict **COM Isolation**:
* **No Direct COM Executions**: The MCP server does not connect directly to active COM sessions or run automation processes.
* **Workflow-Driven Assistant**: The AI's job is to generate a Jupyter Notebook workflow (`.ipynb`) using the `create_jupyter_workflow` tool.
* **User Execution**: You open and run the generated notebook cells inside your active JupyterLab environment (which has the safe connection to Datamine Studio RM).

MCP tools exposed:
* `list_commands`
* `get_command_schema`
* `search_commands`
* `create_jupyter_workflow`

Full registration notes and module details: [AGENTS.md](AGENTS.md).

---

## 🛠️ Developer & Contributor Guide

For developers looking to contribute, run validation tests, or regenerate package wrappers. Depth lives in **[AGENTS.md](AGENTS.md)**; the essentials are below.

### 🧪 Running Test Suites

Before pushing any changes, verify the package using these test scripts:

#### 1. No Datamine License / COM Instance Required

These run smoke tests on Python structures without starting Datamine:

```cmd
.venv\Scripts\python tests\quick_test.py
.venv\Scripts\python tests\test_workflow.py
```

#### 2. Active Datamine Session Required

These tests require Datamine Studio RM to be open with a loaded project:

```cmd
.venv\Scripts\python tests\diagnose_project.py
.venv\Scripts\python tests\stress_test.py
.venv\Scripts\python tests\integration_test.py
.venv\Scripts\python tests\run_sandbox_tests.py
```

### ⚙️ Developer Helper Scripts

* **`tests/generate_wrappers.py`**: Regenerates `dmstudio/dmcommands.py` / `dmfiles.py` (core/verified) and `dmcommands_generated.py` / `dmfiles_generated.py` (experimental) wrapper classes from StudioRM help XML.
* **`tests/generate_collections.py`**: Regenerates individual sandbox notebooks under `tutorials/collections/` for the 23 verified core commands.
* **`tests/restructure_case_studies.py`**: Workflows/case-studies layout helper.
* **`dmstudio.notebook_builder.NotebookBuilder`**: Programmatic Jupyter Notebook builder for auditable agent workflows:

  ```python
  from dmstudio.notebook_builder import NotebookBuilder
  nb = NotebookBuilder('workflow.ipynb', title='My Workflow')
  nb.add_markdown('## Step 1')
  nb.add_code("cmd.mgsort(in_i='collars', out_o='sorted', keys_f=['BHID'])")
  nb.save()
  ```

Changelog: **[CHANGELOG.md](CHANGELOG.md)**. Domain vocabulary: **[CONTEXT.md](CONTEXT.md)**.

---

## ⚖️ License & Attribution

This repository is a combined work licensed under the **GNU General Public License v3.0 (GPL-3.0)**. 

* Original work Copyright (c) 2018 Sean D. Horan — released under [MIT License](LICENSE.txt) (terms preserved at the end of LICENSE.txt).  
* Modifications and new contributions Copyright (c) 2026 Achmad Nazar Abrory — released under GPL-3.0.

See the [LICENSE.txt](LICENSE.txt) file for the full GPL-3.0 text, original MIT terms, and trademark/affiliation disclaimers.
