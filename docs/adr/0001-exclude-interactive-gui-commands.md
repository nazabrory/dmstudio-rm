# ADR-0001: Exclude Interactive and GUI-Only Commands from Python API

## Status

Accepted

## Context

The `dmstudio` package dynamically generates Python wrappers from Datamine Studio RM's XML process help database. However, a set of Datamine commands require manual GUI interaction (wizards, file dialogs, windows explorer popups), full-screen console interaction (e.g. text/database editors), or produce text-based window prints (which block or prompt to save print reports in headless mode).

When these commands are invoked headlessly (such as in automated Jupyter Notebook runs, regression testing, or pipeline runs), they block waiting for user input or graphical confirmation, freezing the main Datamine COM server thread. This leaves the COM automation server locked and unresponsive, requiring a manual process kill of Studio RM.

## Decision

We have decided to completely exclude **36 interactive, GUI-only, statistical display, and report print commands** from the dynamic code generator. Rather than generating functions with warnings (which can still be accidentally called), these functions are omitted during generation, yielding an immediate Python `AttributeError` if called.

The excluded commands are:

1. **GUI / Graphical / Terminal Editors (17 commands):**
   * **AED** (Interactive pad-based database editor)
   * **CLUSTR** (Interactive menu-driven geochemistry cluster analysis)
   * **DMEDIT** (Interactive terminal-like database editor)
   * **ESTIMATE** (Estimate Wizard GUI)
   * **EXPORT** (Interactive Export Driver popup)
   * **HISFIT** (Graphical cursor-based histogram fitting)
   * **LAYOUT** (Graphical cursor-based blast pattern layout design)
   * **LOADCF** (Console macro compilation prompts)
   * **PICTED** (Graphical plot layout editor)
   * **PLTLAY** (Legacy graphical plot editor)
   * **SETENV** (Command-line environment variable merging prompts)
   * **SURLOG** (Interactive survey data logging)
   * **SURVIG** (Graphical multi-window survey editor)
   * **SYSPAR** (Prints parameter metadata to command window, no files used)
   * **VARFIT** (Interactive graphical variogram model fitting)
   * **VER** (Opens version parameters dialog box)
   * **XRUN** (Interactive macro execution console prompts)

2. **Statistical / Print-only (10 commands):**
   * Excluded because they print calculations to the screen or output window and prompt for print reports. In Python, statistics are much better calculated directly on dataframes using `pandas` or `scipy.stats`.
   * **ANOVA1**, **MANOVA**, **ASTRAN**, **DISPLA**, **STATNP**, **SUPES2**, **SUPEST**, **SUPOOB**, **TERPLT**, **ST1GX**

3. **Report / Text Print Generators (8 commands):**
   * Excluded because they generate print layouts and prompt for output destinations. Custom reporting is done using Python.
   * **REPORT**, **REPORK**, **TDOUT**, **TABRES**, **FORMAT**, **PITRES**, **ENGLOG**, **PDRIVE**

4. **Interactive Prompts / Fixed Format Data Entry (1 command):**
   * **EXTNDF** (Prompts interactively for fixed format keyboard entry to extend files)

## Consequences

* **COM Safety:** Headless scripts and automated tutorials can no longer freeze or lock up the Datamine COM server by calling these commands.
* **Omission over warnings:** Omitted commands will fail immediately with `AttributeError` at compile/import time rather than hanging at runtime.
* **Notebook cleanliness:** Obsolete collection notebooks corresponding to these excluded commands have been purged from the repository.
