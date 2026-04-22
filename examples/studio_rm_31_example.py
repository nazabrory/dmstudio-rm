"""
Studio RM 3.1 Example Script
============================

This script demonstrates new capabilities added in Studio RM 3.1
using the updated dmstudio package.

Prerequisites:
--------------
- Active Studio RM 3.1 project
- Valid Datamine license
- Python 3.9+ with dmstudio installed
"""

from dmstudio import dmcommands, dmfiles, initialize, special

# Initialize connection to Studio RM 3.1
cmd = dmcommands.init(version='StudioRM')

# ---------------------------------------------------------------------------
# 1. COPYMOD with retrieval criteria (Studio RM 3.1+)
# ---------------------------------------------------------------------------
# Copy a block model with selective retrieval
cmd.copymod(
    in_i='block_model',
    out_o='high_grade_model',
    retrieval='AU>1.0'
)

# ---------------------------------------------------------------------------
# 2. COMPDH with multiple ZONE and DOM fields (Studio RM 3.1+)
# ---------------------------------------------------------------------------
# Composite drillholes using up to 5 zone fields and dominant categorical values
cmd.compdh(
    in_i='drillhole_samples',
    out_o='composited_dh',
    zone_f='LITHO',
    zone2_f='OXIDE',
    dom1_f='ROCKTYPE',
    interval_p=2.0,
    mincomp_p=1.0
)

# ---------------------------------------------------------------------------
# 3. MODSPLIT with optional outputs (Studio RM 3.1+)
# ---------------------------------------------------------------------------
# Generate only the constrained model output (not fullmod)
cmd.modsplit(
    modelin_i='block_model',
    wiretr_i='orebody_tr',
    wirept_i='orebody_pt',
    modelout_o='ore_model',
    modltype_p=1
)

# ---------------------------------------------------------------------------
# 4. DIGITISE-DOUGHNUT (Studio RM 3.1+)
# ---------------------------------------------------------------------------
# Create closed strings with internal voids
cmd.digitise_doughnut(
    perimeter_i='outer_boundary',
    voids_i='void_strings',
    out_o='doughnut_shape',
    storage_switch_p=1
)

# ---------------------------------------------------------------------------
# 5. SMOOTH-GRADIENT full smoothing (Studio RM 3.1+)
# ---------------------------------------------------------------------------
cmd.smooth_gradient(
    in_i='rough_strings',
    out_o='smoothed_strings',
    mode_p=1
)

# ---------------------------------------------------------------------------
# 6. Automation: Print Plot Sheet to PDF (Studio RM 3.1+)
# ---------------------------------------------------------------------------
oScript = initialize.studio('StudioRM')
special.print_plot_sheet_to_pdf(
    oScript,
    plot_sheet_name="Section_100",
    output_path="C:\\Reports\\Section_100.pdf"
)

# ---------------------------------------------------------------------------
# 7. Automation: Text Importer (Studio RM 3.1+)
# ---------------------------------------------------------------------------
special.text_importer(
    oScript,
    scenario_file="C:\\Import\\drillhole_import.dminsv"
)

# ---------------------------------------------------------------------------
# 8. Update legacy scripts to safer syntax (Studio RM 3.1+)
# ---------------------------------------------------------------------------
cmd.update_scripts(
    path_p="C:\\Scripts\\legacy",
    backup_p=1,
    recursive_p=1
)

print("Studio RM 3.1 example script completed successfully.")
