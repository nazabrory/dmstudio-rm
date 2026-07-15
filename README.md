# dmstudio: Datamine Studio RM Python Scripting

**dmstudio** is a user-friendly Python package designed for geologists and engineers to automate **Datamine Studio RM** workflows. It translates complex Datamine macro syntax into readable, interactive Python commands. The entire workflow is designed to run in interactive **Jupyter Notebooks**, where you can run processes and analyze results step-by-step.

> **Unofficial Disclaimer & Licensing**  
> This is a community-maintained library and is **NOT** an official product of Datamine Software. Datamine Software does not provide support or warranties for this package. 
> 
> This library uses official Datamine COM Automation APIs (`Datamine.StudioRM.Application` and `DmFile.DmTableADO`) which are built into Studio RM. To run the automation, you **must already own a valid, licensed instance** of Datamine Studio RM running on your system. This library does not bypass or clone any Datamine proprietary code.

---

## 📋 Step-by-Step Setup: Starting from Scratch

If you have a Datamine working folder and want to use this scripting framework, follow this step-by-step guide.

### Step 1: Open Your Datamine Project
1. Open **Datamine Studio RM** on Windows.
2. Load your project. If you are starting fresh, create a new project and save it to a folder on your drive (e.g., `C:\DatamineProjects\MyMineProject`).
3. Make sure you know the absolute path of this working directory.

### Step 2: Keep the Repository in a Single Separate Folder
To prevent cluttering your actual project folder with library source code, configuration files, and setup scripts:
1. Clone or download this repository into a separate folder on your machine (e.g., `C:\DatamineTools\dmstudio-rm3`).
2. Keep your own Datamine project files and actual geological database inside your own clean project folder (e.g., `C:\DatamineProjects\MyMineProject`).
3. This ensures your project folder remains clean, like this:
   ```
   C:\DatamineProjects\MyMineProject\   <-- Your actual project folder (pristine & tidy)
   ├── MyProject.rmproj                 (Your Datamine project file)
   ├── high_grade_assays.dm             (Your output/input data files)
   └── sorted_assays.dm
   ```

### Step 3: Install the Package in Your Environment
By installing the library in "editable mode" (`-e`), the Python environment will know how to load `dmstudio` from any directory without needing to copy the package folder into your project folder.

1. Open your terminal or Command Prompt.
2. Navigate to the folder where you cloned this repository:
   ```cmd
   cd C:\DatamineTools\dmstudio-rm3
   ```
3. Choose one of the environment options below to set up and install the package:

#### Option A: Using Conda (Recommended)
```cmd
# Create and activate environment
conda create --name dmstudio python=3.9 -y
conda activate dmstudio

# Install dependencies and install package in editable mode
conda install -y pandas numpy nbformat -c conda-forge
pip install pywin32 mcp
pip install -e .
```

#### Option B: Using Pip and Virtual Environments (Standard)
```cmd
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies and install package in editable mode
pip install -r requirements.txt
pip install -e .
```

### Step 4: Run the Connection Diagnostic
Before scripting, verify that Python can talk to your running Studio RM session:
1. Make sure your Datamine project is open and active in Studio RM.
2. Open your terminal (with your environment active) and run:
   ```cmd
   python tests/diagnose_project.py
   ```
3. If it outputs `[SUCCESS] Project found!`, you are fully prepared to automate your workflow.

---

## 🚀 How to Run the Jupyter Notebook Tutorials

Instead of writing scripts or typing in the terminal, you can run everything inside interactive notebooks. 

To open the tutorials:
1. Open your terminal in your project folder.
2. Activate your environment (Conda: `conda activate dmstudio` / Pip: `.venv\Scripts\activate`).
3. Start the Jupyter Notebook interface:
   ```cmd
   jupyter notebook
   ```
4. A browser window will open automatically. Navigate to the `tutorials/` folder and click on **`Holes3D_Tutorial.ipynb`** (Recommended) to run a complete drillhole de-surveying workflow.

---

## 💡 How it Works (Simple Python Example)

Instead of complex Datamine scripting, you write clear, self-explanatory Python commands inside your notebook cells:

```python
from dmstudio import dmcommands

# 1. Connect to your open Studio RM project
cmd = dmcommands.init(version='StudioRM')

# 2. Sort drillhole assays by Hole ID (BHID) and Depth (FROM)
cmd.mgsort(in_i='assays', out_o='sorted_assays', keys_f=['BHID', 'FROM'])

# 3. Filter for samples with grade greater than 1.5
cmd.copy(in_i='sorted_assays', out_o='high_grade_assays', retrieval="AU > 1.5")
```

### Suffix Guide for Datamine Users
* `_i` = **Input File** (e.g. `in_i='assays'`)
* `_o` = **Output File** (e.g. `out_o='sorted_assays'`)
* `_f` = **Fields** (e.g. `keys_f=['BHID']`)
* `_p` = **Parameters** (e.g. `interval_p=2.0`)

---

## 🤖 How to Use the AI Capabilities (Step-by-Step)

This repo supports the Model Context Protocol (MCP) to let AI assistants (like Claude Desktop or Google Antigravity) control Datamine and generate notebooks for you.

Here is how to set up and use the AI:

### Step 1: Register the MCP Server with Your AI Client

#### For Claude Desktop:
1. Open the Claude Desktop configuration file:
   `%APPDATA%\Claude\claude_desktop_config.json`
2. Add `dmstudio` to the `mcpServers` list (use absolute paths to your python executable and `mcp_server.py`):
   ```json
   {
     "mcpServers": {
       "dmstudio": {
         "command": "C:\\DatamineProjects\\MyMineProject\\.venv\\Scripts\\python.exe",
         "args": ["C:\\DatamineProjects\\MyMineProject\\mcp_server.py"]
       }
     }
   }
   ```
   *(If you are using a Conda environment, replace the command path with your Conda environment python path, e.g. `C:\\Users\\<username>\\miniconda3\\envs\\dmstudio\\python.exe`)*
3. Restart Claude Desktop. You will see a plug icon indicating the `dmstudio` tools are loaded.

#### For Google Antigravity:
Add the server config to `.gemini/config/antigravity.json` using the same JSON format shown above.

---

### Step 2: Open Your Datamine Project
1. Open Datamine Studio RM.
2. Load your project (e.g. `tutorials/Project.rmproj`). Keep it open in the background.

---

### Step 3: Ask the AI to Automate Workflows
You can now ask the AI conversational prompts. The AI will query the Datamine API definitions and generate clean notebooks for you.

**Example Prompts to Try:**
* *"What Datamine commands are available in this repo?"*
* *"Show me the parameters required for the MGSORT command."*
* *"Search for commands related to drillhole composition."*
* *"Create a Jupyter notebook workflow called `desurvey_flow.ipynb` that loads `_vb_collars` and `_vb_surveys`, runs the DESURV command, and saves the output to `dholes`."*

---

### Step 4: Run & Edit the AI-Generated Notebook

When you ask the AI to generate a workflow, it does not execute the Datamine commands directly (which might fail or mess up your workspace). Instead, it creates the notebook file directly in your project directory. You can run, inspect, and edit it:

#### Option A: Direct Chat via VS Code Plugins / Terminal Agents (Cursor, Copilot, Roo Code, Claude Code)
If you are using an AI coding agent running directly inside your VS Code workspace or terminal:
- **No MCP Setup Needed**: Since these agents have direct access to your project workspace files, they do not need the MCP server setup. They can read `AGENTS.md` and `README.md` to understand the Python scripting package automatically.
- **Workflow Generation**: Ask your agent in chat or terminal: *"Create a Jupyter Notebook `tutorials/my_flow.ipynb` that loads the survey database, runs MGSORT on BHID, and performs DESURV."* The agent will write the notebook directly using the `NotebookBuilder` utility.
- **Workspace Data Exploration**: You can ask the agent to inspect your project files first: *"Import `dmstudio.agent` and read the first 5 rows of `tutorials/_vb_assays.dmx` to see what columns we have, then write a compositing workflow notebook."*
- **Execution & Audit**: Open the generated notebook inside VS Code, choose your virtual environment (`.venv`) or Conda environment (`dmstudio`) as the kernel, and run cells individually. You can review, modify, and execute cells interactively.

#### Option B: Registering as MCP Server (Claude Desktop / Antigravity)
If you are using external AI applications (like Claude Desktop or Google Antigravity):
1. Configure your client configuration files (Step 1).
2. The AI will call the `create_jupyter_workflow` tool to write the notebook file directly to your project directory.
3. Open the notebook in your browser or VS Code:
   ```cmd
   jupyter notebook tutorials/desurvey_flow.ipynb
   ```
4. Run the cells step-by-step to execute the Datamine commands. This keeps the AI workflow **fully transparent and auditable**.

---

## ⚖️ License & Attribution

Original work Copyright (c) 2018 Sean D. Horan — released under [MIT License](LICENSE.txt).  
Modifications and new contributions Copyright (c) 2025 nazabrory contributors.

The MIT license permits modification and redistribution provided the original copyright notice is preserved. See [LICENSE.txt](LICENSE.txt) for full terms.
