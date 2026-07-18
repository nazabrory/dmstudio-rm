import os
import shutil
import json

def restructure_case_studies():
    print("Starting workflows restructuring...")
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tutorials_dir = os.path.join(base_dir, 'tutorials')
    workflows_dir = os.path.join(tutorials_dir, 'workflows')
    os.makedirs(workflows_dir, exist_ok=True)
    
    project_template = os.path.join(tutorials_dir, 'Project.rmproj')
    if not os.path.exists(project_template):
        raise FileNotFoundError(f"Project template not found at: {project_template}")
        
    # Verification check code template to insert
    ver_check_lines = [
        "\n",
        "# Verify that the active project matches this folder (case-insensitive) to prevent writing files to the wrong place\n",
        "import os\n",
        "notebook_folder = os.path.normpath(os.path.dirname(os.path.abspath('__file__'))).lower()\n",
        "active_folder = os.path.normpath(oScript.ActiveProject.Folder).lower()\n",
        "if active_folder != notebook_folder:\n",
        "    raise RuntimeError(\n",
        "        f\"Active Datamine Project ({active_folder}) does not match this notebook's folder ({notebook_folder}).\\n\"\n",
        "        \"Please open the 'Project.rmproj' in this folder inside Datamine Studio RM first!\"\n",
        "    )\n",
        "print(\"Active project verified successfully.\")"
    ]

    # 1. Holes3D Case Study
    holes3d_dest_dir = os.path.join(workflows_dir, 'holes3d_desurvey')
    os.makedirs(holes3d_dest_dir, exist_ok=True)
    
    shutil.copy(project_template, os.path.join(holes3d_dest_dir, 'Project.rmproj'))
    for f_name in ['_vb_assays.dmx', '_vb_collars.dmx', '_vb_lithology.dmx', '_vb_surveys.dmx']:
        src = os.path.join(tutorials_dir, f_name)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(holes3d_dest_dir, f_name))
            
    src_holes3d = os.path.join(tutorials_dir, 'Holes3D_Tutorial.ipynb')
    if os.path.exists(src_holes3d):
        with open(src_holes3d, 'r', encoding='utf-8') as f_in:
            nb = json.load(f_in)
        # Modify the first code cell to include verification check
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'code':
                # This is Step 1 code cell
                if any('initialize.studio' in line for line in cell.get('source', [])):
                    cell['source'].extend(ver_check_lines)
                    break
        with open(os.path.join(holes3d_dest_dir, 'Holes3D_Tutorial.ipynb'), 'w', encoding='utf-8') as f_out:
            json.dump(nb, f_out, indent=1)
        print("Set up holes3d_desurvey case study.")

    # 2. Grade Estimation Case Study
    grade_dest_dir = os.path.join(workflows_dir, 'grade_estimation')
    os.makedirs(grade_dest_dir, exist_ok=True)
    
    shutil.copy(project_template, os.path.join(grade_dest_dir, 'Project.rmproj'))
    src_comp = os.path.join(tutorials_dir, 'comp_holes.dmx')
    if os.path.exists(src_comp):
        shutil.copy(src_comp, os.path.join(grade_dest_dir, 'comp_holes.dmx'))
        
    src_grade = os.path.join(tutorials_dir, 'Grade_Estimation_Examples.ipynb')
    if os.path.exists(src_grade):
        with open(src_grade, 'r', encoding='utf-8') as f_in:
            nb = json.load(f_in)
        
        # Modify code cells: active project check, relative database paths
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'code':
                src_lines = cell.get('source', [])
                # Cell 1: Connect to Studio RM
                if any('initialize.studio' in line for line in src_lines):
                    src_lines.extend(ver_check_lines)
                # Cell 3: Parameter files setup
                new_source = []
                for line in src_lines:
                    if 'help_db = r"D:\\Active\\dmstudio\\datamine_help\\Database\\DMTutorials\\Data\\VBOP\\Datamine"' in line:
                        new_source.append("repo_root = os.path.abspath(os.path.join(project_folder, '..', '..', '..'))\n")
                        new_source.append("help_db = os.path.join(repo_root, 'datamine_help', 'Database', 'DMTutorials', 'Data', 'VBOP', 'Datamine')\n")
                    else:
                        new_source.append(line)
                cell['source'] = new_source
                
        with open(os.path.join(grade_dest_dir, 'Grade_Estimation_Examples.ipynb'), 'w', encoding='utf-8') as f_out:
            json.dump(nb, f_out, indent=1)
        print("Set up grade_estimation case study.")

    # 3. Studio RM Examples
    examples_dest_dir = os.path.join(workflows_dir, 'studio_rm_examples')
    os.makedirs(examples_dest_dir, exist_ok=True)
    
    shutil.copy(project_template, os.path.join(examples_dest_dir, 'Project.rmproj'))
    src_ex = os.path.join(tutorials_dir, 'Studio_RM_3.1_Examples.ipynb')
    if os.path.exists(src_ex):
        with open(src_ex, 'r', encoding='utf-8') as f_in:
            nb = json.load(f_in)
        for cell in nb.get('cells', []):
            if cell.get('cell_type') == 'code':
                src_lines = cell.get('source', [])
                if any("initialize.studio('StudioRM')" in line for line in src_lines):
                    # Need to declare oScript before verify check
                    # Cell might not have oScript = initialize.studio('StudioRM') but cmd = ... and then oScript later.
                    # Let's check if oScript is in the cell.
                    if not any("oScript = " in line for line in src_lines):
                        new_lines = [
                            "\n",
                            "oScript = initialize.studio('StudioRM')\n"
                        ] + ver_check_lines
                    else:
                        new_lines = ver_check_lines
                    src_lines.extend(new_lines)
        with open(os.path.join(examples_dest_dir, 'Studio_RM_3.1_Examples.ipynb'), 'w', encoding='utf-8') as f_out:
            json.dump(nb, f_out, indent=1)
        print("Set up studio_rm_examples case study.")
        
    # Cleanup old root files
    print("Cleaning up old files in tutorials/ root folder...")
    old_files = [
        'Holes3D_Tutorial.ipynb',
        'Grade_Estimation_Examples.ipynb',
        'Studio_RM_3.1_Examples.ipynb',
        '_vb_assays.dmx',
        '_vb_collars.dmx',
        '_vb_lithology.dmx',
        '_vb_surveys.dmx',
        'comp_holes.dmx',
        'dholes.dmx',
        'estimation_params.dmx',
        'grade_model_cokrig.dmx',
        'grade_model_cokrig_result.dmx',
        'grade_model_estima.dmx',
        'grade_model_estima_result.dmx',
        'kriging_epar.dmx',
        'kriging_epar_min.dmx',
        'kriging_epar_nn.dmx',
        'kriging_fields.dmx',
        'kriging_fields_min.dmx',
        'kriging_fields_nn.dmx',
        'kriging_spar.dmx',
        'kriging_vmodel.dmx',
        'model_proto.dmx',
        'search_params.dmx',
        'temp1.dmx',
        'temp2.dmx',
        'tempassays.dmx',
        'tempcollar.dmx',
        'templith.dmx',
        'tempsurvey.dmx',
        'drillhole_visualization.html'
    ]
    for f_name in old_files:
        path = os.path.join(tutorials_dir, f_name)
        if os.path.exists(path):
            try:
                os.remove(path)
                print(f"Removed old file: {f_name}")
            except Exception as e:
                print(f"Error removing {f_name}: {e}")
                
    print("Workflows restructuring complete!")

if __name__ == '__main__':
    restructure_case_studies()
