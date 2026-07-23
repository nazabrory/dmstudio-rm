import json
import os

def patch_join():
    path = r'D:\Active\dmstudio-rm\tutorials\collections\join_example.ipynb'
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            source_str = "".join(cell.get('source', []))
            
            # Patch Step 3
            if '# Step 3: Copy VBOP datasets dynamically' in source_str:
                cell['source'] = [
                    "# Step 3: Copy VBOP datasets dynamically from Database to test_sandbox\n",
                    "files_to_copy = [\n",
                    "    \"_vb_assays.dmx\",\n",
                    "    \"_vb_collars.dmx\"\n",
                    "]\n",
                    "\n",
                    "agent.copy_database_files(files_to_copy)\n",
                    "\n",
                    "# Sort inputs using mgsort to ensure sort flags are correctly set in the file headers\n",
                    "print(\"Sorting input files with mgsort...\")\n",
                    "dm_cmd.mgsort(\n",
                    "    in_i='t_assays',\n",
                    "    out_o='t_assays_sorted',\n",
                    "    keys_f=['BHID']\n",
                    ")\n",
                    "dm_cmd.mgsort(\n",
                    "    in_i='t_collars',\n",
                    "    out_o='t_collars_sorted',\n",
                    "    keys_f=['BHID']\n",
                    ")\n",
                    "print(\"Prepared sorted assays and collars files by BHID.\")"
                ]
            
            # Patch Step 4
            elif '# Execute join' in source_str:
                cell['source'] = [
                    "# Execute join on sorted assays and collars\n",
                    "print(\"Running join...\")\n",
                    "dm_cmd.join(\n",
                    "    inmods_i=['t_assays_sorted', 't_collars_sorted'],  # required\n",
                    "    out_o='t_join_out',  # required\n",
                    "    keys_f=['BHID'],  # required keyfield\n",
                    "    # subsetr_p=0,  # optional\n",
                    "    # subsetf_p=0,  # optional\n",
                    "    # cartjoin_p=0,  # optional\n",
                    "    # keytol_p=1e-05,  # optional\n",
                    "    # print_p=0,  # optional\n",
                    "    # arguments='optional',  # optional\n",
                    "    # retrieval='optional',  # optional\n",
                    ")\n",
                    "print(\"join execution completed.\")"
                ]

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print("Patched join_example.ipynb successfully.")

def patch_diffrn():
    path = r'D:\Active\dmstudio-rm\tutorials\collections\diffrn_example.ipynb'
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'code':
            source_str = "".join(cell.get('source', []))
            
            # Patch Step 3
            if '# Step 3: Copy VBOP datasets dynamically' in source_str:
                cell['source'] = [
                    "# Step 3: Copy VBOP datasets dynamically from Database to test_sandbox\n",
                    "files_to_copy = [\n",
                    "    \"_vb_assays.dmx\"\n",
                    "]\n",
                    "\n",
                    "agent.copy_database_files(files_to_copy)\n",
                    "\n",
                    "# Read assays and subset them\n",
                    "df_all = agent.read_datamine('t_assays.dmx')\n",
                    "df_del = df_all[df_all['BHID'] == 'VB2737']\n",
                    "\n",
                    "# Save temporary files for sorting\n",
                    "agent.to_datamine(df_all, 't_assays_all_unsorted.dmx')\n",
                    "agent.to_datamine(df_del, 't_assays_del_unsorted.dmx')\n",
                    "\n",
                    "# Sort both files using mgsort to ensure sorting headers are set correctly for diffrn\n",
                    "print(\"Sorting files with mgsort...\")\n",
                    "dm_cmd.mgsort(\n",
                    "    in_i='t_assays_all_unsorted',\n",
                    "    out_o='t_assays_all',\n",
                    "    keys_f=['BHID']\n",
                    ")\n",
                    "dm_cmd.mgsort(\n",
                    "    in_i='t_assays_del_unsorted',\n",
                    "    out_o='t_assays_del',\n",
                    "    keys_f=['BHID']\n",
                    ")\n",
                    "print(\"Prepared t_assays_all.dmx and t_assays_del.dmx (sorted by BHID via mgsort).\")"
                ]
            
            # Patch Step 4
            elif '# Execute diffrn' in source_str:
                cell['source'] = [
                    "# Execute diffrn on sorted files\n",
                    "print(\"Running diffrn...\")\n",
                    "dm_cmd.diffrn(\n",
                    "    inmods_i=['t_assays_all', 't_assays_del'],  # required\n",
                    "    out_o='t_diffrn_out',  # required\n",
                    "    keys_f=['BHID'],  # required keyfield\n",
                    "    # keytol_p=1e-05,  # optional\n",
                    "    # arguments='optional',  # optional\n",
                    "    # retrieval='optional',  # optional\n",
                    ")\n",
                    "print(\"diffrn execution completed.\")"
                ]

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print("Patched diffrn_example.ipynb successfully.")

if __name__ == '__main__':
    patch_join()
    patch_diffrn()
