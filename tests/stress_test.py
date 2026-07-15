import sys
import os

# Add parent directory to path so dmstudio is importable when run from tests/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import traceback
from dmstudio import dmcommands, dmfiles, initialize

def run_stress_test():
    print("="*60)
    print("DMSTUDIO END-TO-END STRESS TEST WITH REAL STUDIO CONNECTION")
    print("="*60)
    
    # 1. Connect to Studio
    print("1. Initializing connection to Studio RM...")
    try:
        oScript = initialize.studio('StudioRM')
        print(f"   [OK] Connected: {oScript.Caption}")
    except Exception as e:
        print(f"   [FAIL] Could not connect to Studio RM. Make sure Studio RM is running with a project loaded.")
        print(f"   Error details: {e}")
        sys.exit(1)
        
    # Clear any active commands/dialogs in Studio
    print("   Clearing any active commands in Studio...")
    import win32gui
    import win32con
    import time
    
    def dismiss_studio_dialogs():
        dlg_hwnds = []
        def enum_dlgs(hwnd, extra):
            if win32gui.GetWindowText(hwnd) == "Studio RM" and win32gui.GetClassName(hwnd) == "#32770":
                dlg_hwnds.append(hwnd)
            return True
        win32gui.EnumWindows(enum_dlgs, None)
        
        for dlg in dlg_hwnds:
            yes_btn = None
            def find_yes(hwnd, extra):
                nonlocal yes_btn
                if "Yes" in win32gui.GetWindowText(hwnd):
                    yes_btn = hwnd
                    return False
                return True
            win32gui.EnumChildWindows(dlg, find_yes, None)
            if yes_btn:
                print(f"   [CLEANUP] Found modal dialog and clicking Yes button (handle {yes_btn})...")
                win32gui.SendMessage(yes_btn, win32con.BM_CLICK, 0, 0)
                time.sleep(0.5)

    dismiss_studio_dialogs()
    for _ in range(3):
        try:
            oScript.Parsecommand("can")
        except Exception as e:
            if "running" in str(e):
                dismiss_studio_dialogs()
                try:
                    oScript.Parsecommand("can")
                except:
                    pass
        
    # 2. Get project details and set directory
    print("\n2. Querying project properties...")
    project = oScript.ActiveProject
    if project is None:
        print("   [FAIL] No active project found in Studio RM COM context.")
        sys.exit(1)
        
    project_dir = project.Folder
    print(f"   [OK] Active Project: {project.Title}")
    print(f"   [OK] Project Path: {project.FilePath}")
    print(f"   [OK] Project Folder: {project_dir}")
    
    # Change working directory to project folder
    os.chdir(project_dir)
    print(f"   [OK] Python working directory changed to: {project_dir}")
    
    # Register the source database file in the project tree via COM to avoid path spaces and slash splitting in CLI
    raw_db_path = os.path.join(project_dir, 'Database', 'DMTutorials', 'Data', 'VBOP', 'Datamine', '_vb_assays.dmx')
    print(f"   Registering source database file in project: {raw_db_path}")
    try:
        project.AddFile(raw_db_path)
        time.sleep(0.5)
        dismiss_studio_dialogs()
    except Exception as add_e:
        print(f"   [WARN] AddFile failed: {add_e}")
        
    db_assays_path = '_vb_assays'
    print(f"   [OK] Target database assays path logical name: {db_assays_path}")
    
    # Initialize command wrapper instances
    cmd = dmcommands.init('StudioRM')
    
    # List of files we will create and clean up
    temp_files = []
    
    def register_temp_file(basename):
        basename = basename.strip("'")
        temp_files.append(basename + '.dm')
        temp_files.append(basename + '.dmx')
        temp_files.append(basename + '.dm.key')
        temp_files.append(basename + '.dmx.key')
        
    try:
        # 3. Copy database file to project workspace
        print("\n3. Running COPY command...")
        local_assays = 'stress_temp_local_assays'
        register_temp_file(local_assays)
        cmd.copy(in_i=db_assays_path, out_o=local_assays)
        print(f"   [OK] Copied {db_assays_path} to {local_assays}")
        time.sleep(1.0)
        
        # 4. Sort local assays using MGSORT
        print("\n4. Running MGSORT command...")
        sorted_assays = 'stress_temp_sorted_assays'
        register_temp_file(sorted_assays)
        cmd.mgsort(in_i=local_assays, out_o=sorted_assays, keys_f=['BHID', 'FROM'])
        print(f"   [OK] Sorted assays saved as {sorted_assays}")
        time.sleep(1.0)
        
        # 5. Filter for high-grade assays using COPY with retrieval
        print("\n5. Running COPY with retrieval (AU > 1.5)...")
        high_grade_assays = 'stress_temp_hg_assays'
        register_temp_file(high_grade_assays)
        cmd.copy(in_i=sorted_assays, out_o=high_grade_assays, retrieval="AU > 1.5")
        print(f"   [OK] High grade assays saved as {high_grade_assays}")
        time.sleep(1.0)
        
        # 6. Run summary STATS on high-grade assays
        print("\n6. Running STATS command...")
        stats_out = 'stress_temp_stats_out'
        register_temp_file(stats_out)
        # Note: fields_f takes a list of strings, so we pass ['AU']
        cmd.stats(in_i=high_grade_assays, out_o=stats_out, fields_f=['AU'])
        # Save the project to flush memory-cached tables to disk
        print("   Saving project to flush files to disk...")
        try:
            project.Save()
            time.sleep(1.0)
        except Exception as save_e:
            print(f"   [WARN] Project Save failed: {save_e}")
            
        # 7. Verify stats table existence
        print("\n7. Verifying stats output file exists on disk...")
        # Use clean stats_out name for check
        clean_stats_out = stats_out.strip("'")
        print(f"   [DEBUG] Files in active project folder starting with 'stress_temp_': {[f for f in os.listdir(project_dir) if 'stress_temp_' in f]}")
        try:
            print(f"   [DEBUG] Datamine reports stats path as: {project.GetFilePathFromFileName(stats_out)}")
        except Exception as query_e:
            print(f"   [DEBUG] Query path failed: {query_e}")
            
        stats_out_exists = False
        for ext in ['.dm', '.dmx']:
            target_path = os.path.join(project_dir, clean_stats_out + ext)
            if os.path.exists(target_path):
                stats_out_exists = True
                print(f"   [OK] Found generated stats file: {target_path}")
                break
                
        # Alternative database existence check
        if not stats_out_exists:
            try:
                if project.DBObjExists(clean_stats_out) or project.ContainsFile(clean_stats_out) or project.ContainsFile(clean_stats_out + '.dmx'):
                    stats_out_exists = True
                    print(f"   [OK] Found generated stats file in Datamine database context")
            except Exception as exists_e:
                print(f"   [DEBUG] Database existence check failed: {exists_e}")
        
        if not stats_out_exists:
            print(f"   [FAIL] Generated stats table {clean_stats_out} not found on disk or database!")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n[FAIL] Stress test encountered an error: {e}")
        traceback.print_exc()
        sys.exit(1)
    finally:
        # 9. Clean up temporary files from project directory
        print("\n9. Cleaning up temporary files...")
        cleanup_count = 0
        for temp_file in temp_files:
            target_path = os.path.join(project_dir, temp_file)
            if os.path.exists(target_path):
                try:
                    os.remove(target_path)
                    cleanup_count += 1
                except Exception as clean_e:
                    print(f"   [WARN] Could not delete {target_path}: {clean_e}")
        print(f"   [OK] Deleted {cleanup_count} temporary files.")
        
    print("\n" + "="*60)
    print("STRESS TEST COMPLETED SUCCESSFULLY!")
    print("="*60)

if __name__ == "__main__":
    run_stress_test()
