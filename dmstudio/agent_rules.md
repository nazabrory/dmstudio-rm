---
name: dmstudio-rules
description: Critical rules, constraints, and standard workflows for AI agents scripting Datamine Studio RM via dmstudio.
---

# Datamine Studio RM AI Agent Rules

This document outlines the critical rules, constraints, and standard workflows for AI agents writing Python scripts or Jupyter Notebooks to automate Datamine Studio RM via the `dmstudio` library.

---

## 1. Project Directory Isolation

Datamine Studio RM COM automation is strictly bound to the active project folder. Failing to respect this boundary will result in data access failures, parser crashes, or silent command failures.

- **Always Work Within the Active Project Folder**:
  - All input files (e.g. `in_i`, `in1_i`) and output files (e.g. `out_o`, `out1_o`) must reside in the active project directory.
  - Reference files using **logical names** (e.g., `'sorted_holes'`, `'model_proto'`) rather than absolute Windows file paths.
- **Handling External Files**:
  - If you need to read or pull data from an external location, do NOT pass the absolute path directly to a Datamine command wrapper.
  - Instead, register the external file into the active project first using:
    ```python
    # Add external file to the active project
    oScript = initialize.studio('StudioRM')
    oScript.ActiveProject.AddFile(absolute_path)
    ```
  - After adding, refer to the file solely by its logical name (e.g., `'my_external_data'`) in all subsequent command wrappers.

---

## 2. Command Data Dependencies & Prior Sorting

Certain Datamine Studio RM processes will fail or throw errors if the input tables are not sorted in a specific order before execution.

- **Sort Before Estimating/Evaluating**:
  - Processes like **`ESTIMATE`**, **`COKRIG`**, and wireframe/block-model evaluation expect data to be sorted on specific key fields (such as `IJK` for block models, or spatial coordinate fields `X`, `Y`, `Z` for samples).
  - Always check if the input dataset requires sorting. If so, run the sorting command first:
    ```python
    # Example: Sorting a block model by key fields before grade estimation
    dm_cmd.mgsort(
        in_i='block_model',
        out_o='sorted_block_model',
        keys_f=['IJK']
    )
    ```

---

## 3. Coordinate System & Bounding Box Alignment

All spatial objects (drillholes, block models, wireframes, strings) participating in a workflow must reside in the same coordinate system and have overlapping spatial extents.

- **Check Bounding Boxes**:
  - Before performing estimation, evaluation, or wireframe cutting, verify that the bounding boxes of the objects overlap.
  - If a block model prototype is being defined via **`PROTOM`**, it must cover the exact spatial bounding box of the input drillhole samples. Check the sample coordinates first (e.g., by reading the `.dm` file using `read_datamine` and calculating pandas `min()` and `max()` on `X`, `Y`, `Z` columns) and set the prototype origin, cell size, and cell count accordingly.
- **Coordinate Homogeneity**:
  - Never mix datasets from different coordinate systems (e.g., local mine grid vs. UTM) without running conversion processes.

---

## 4. Critical COM Engineering Constraints

To prevent crashes and hangs in the COM automation layer, adhere to these technical rules:

- **No Backslashes in CLI Commands**:
  - Windows backslashes (`\`) break the internal Datamine command parser `Parsecommand()`. Never pass absolute paths containing backslashes as arguments to commands. Use logical names.
- **No Spaces in Paths**:
  - Spaces in command arguments will break the Datamine command parser. Use `ActiveProject.AddFile()` to register files with spaces in their paths.
- **Scratch Files (Leading Underscore)**:
  - Logical names with a leading underscore (e.g. `'_temp_file'`) are treated as in-memory scratch files. They are not written to disk. Use non-`_` names for durable outputs that you wish to inspect or keep.
- **Avoid Hanging Dialogs**:
  - `Parsecommand()` runs on the main application thread. If a command triggers an interactive UI dialog prompt, the automation will hang indefinitely.
  - Wrap any command that might trigger a popup inside the `dialog_dismiss_context`:
    ```python
    from dmstudio.dialog import dialog_dismiss_context
    
    with dialog_dismiss_context():
        dm_cmd.some_command(...)
    ```
- **1-Indexed Datamine Tables**:
  - Field schemas and columns in `DmFile.DmTableADO` are 1-indexed. Keep this in mind when querying fields programmatically.

---

## 5. MCP Decoupled Workflow Policy

- **No Direct COM Executions from MCP Server**:
  - The MCP server does not own an active COM session to prevent file locks, multi-process clashes, and application crashes.
  - Do NOT call COM commands inside MCP tools. Instead, construct a Jupyter Notebook workflow (`.ipynb`) using the `create_jupyter_workflow` tool, allowing the user to inspect, audit, and execute it within their running Datamine environment.
