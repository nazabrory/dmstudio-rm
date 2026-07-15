# dmstudio: Datamine Studio RM Python Scripting

**dmstudio** is a user-friendly Python package designed for geologists and engineers to automate **Datamine Studio RM** workflows. It translates complex Datamine macro syntax into readable, interactive Python commands.

No programming background is required! The entire workflow is designed to run in interactive **Jupyter Notebooks**, where you can run processes and analyze results step-by-step with a single click.

---

## 🚀 Quick Start Guide (For Geologists)

### 1. Requirements
* Windows OS with **Datamine Studio RM** installed.
* An active Datamine Studio license.
* Python installed (if you don't have it, download the latest version from [python.org](https://www.python.org/downloads/)).

### 2. One-Click Setup
We have provided setup scripts that automatically create a clean environment and install all package requirements:

* **Option A (Command Prompt):** Double-click or run `setup_env.bat`
* **Option B (PowerShell):** Run `.\setup_env.ps1`

---

## 📓 Interactive Jupyter Notebook Tutorials

Instead of writing scripts or typing in the terminal, you can learn and run everything inside interactive notebooks. 

To open the tutorials:
1. Open your terminal/command prompt in this folder.
2. Activate the environment:
   ```cmd
   .venv\Scripts\activate
   ```
3. Start the Jupyter Notebook interface:
   ```cmd
   jupyter notebook
   ```

A browser window will open automatically. Click on either of the two pre-loaded notebooks:

1. **`Holes3D_Tutorial.ipynb`** (Recommended)
   - A complete walk-through of the official Datamine drillhole de-surveying workflow.
   - Learns how to load **Collars, Assays, Lithology, and Surveys**, sort them, merge them, run `DESURV`, and view the results in a tabular view.
2. **`examples/Studio_RM_3.1_Examples.ipynb`**
   - Shows advanced features in Studio RM 3.1 & 3.2+ like compositing (`COMPDH`), model splitting (`MODSPLIT`), printing plot sheets to PDF, and Text Importer automation.

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

### Prefix Guide for Datamine Users
If you are familiar with Datamine commands, the input variables map directly using these simple suffixes:
* `_i` = **Input File** (e.g. `in_i='assays'`)
* `_o` = **Output File** (e.g. `out_o='sorted_assays'`)
* `_f` = **Fields** (e.g. `keys_f=['BHID']`)
* `_p` = **Parameters** (e.g. `interval_p=2.0`)

---

## 🤖 AI Agent & MCP Support (Advanced)

If you are using AI tools (such as Claude Desktop or Google Antigravity) to help you build Datamine workflows:

1. **Jupyter Notebook Builder**: The package includes a `NotebookBuilder` that allows AI agents to write the entire workflow to a Jupyter Notebook first, keeping the execution fully transparent and auditable by you before it runs.
2. **MCP Server**: Run `mcp_server.py` to expose all Datamine commands, parameters, and schema details directly to your AI client as tools.

See [HANDOFF.md](HANDOFF.md) for full developer specifications and setup instructions.

---

## ⚖️ License & Attribution

Original work Copyright (c) 2018 Sean D. Horan — released under [MIT License](LICENSE.txt).  
Modifications and new contributions Copyright (c) 2025 nazabrory contributors.

The MIT license permits modification and redistribution provided the original copyright notice is preserved. See [LICENSE.txt](LICENSE.txt) for full terms.
