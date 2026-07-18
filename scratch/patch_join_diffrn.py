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
                    "# Read and sort inputs on BHID to prepare for relational join\n",
                    "df_assays = agent.read_datamine('t_assays.dmx')\n",
                    "df_collars = agent.read_datamine('t_collars.dmx')\n",
                    "\n",
                    "df_assays_sorted = df_assays.sort_values(by='BHID')\n",
                    "df_collars_sorted = df_collars.sort_values(by='BHID')\n",
                    "\n",
                    "agent.to_datamine(df_assays_sorted, 't_assays_sorted.dmx')\n",
                    "agent.to_datamine(df_collars_sorted, 't_collars_sorted.dmx')\n",
                    "print(\"Prepared and sorted assays and collars files by BHID.\")"
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
                    "# Read assays and sort by BHID\n",
                    "df_all = agent.read_datamine('t_assays.dmx')\n",
                    "df_all_sorted = df_all.sort_values(by='BHID')\n",
                    "\n",
                    "# Create a subset to delete (e.g., BHID == 'VB2737')\n",
                    "df_del = df_all_sorted[df_all_sorted['BHID'] == 'VB2737']\n",
                    "\n",
                    "# Save them\n",
                    "agent.to_datamine(df_all_sorted, 't_assays_all.dmx')\n",
                    "agent.to_datamine(df_del, 't_assays_del.dmx')\n",
                    "print(\"Prepared t_assays_all.dmx and t_assays_del.dmx (sorted by BHID).\")"
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
