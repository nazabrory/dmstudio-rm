# Datamine Studio RM Macro Initialization Script
# Run this from within Studio RM via: Tools > Macro > Run Python Script
# This registers the project in the COM Running Object Table (ROT)

import os

def main():
    # In Studio RM scripting context, 'oScript' is automatically injected into the global namespace.
    # We check if it exists in globals()
    if 'oScript' not in globals():
        print("This script must be run from inside Datamine Studio RM.")
        return

    print("Connected successfully inside Datamine Studio RM!")
    print(f"Application Caption: {oScript.Caption}")
    print(f"Application Version: {oScript.Version}")

    project = oScript.ActiveProject
    if project is not None:
        print(f"Active Project Name: {project.Name}")
        print(f"Active Project Folder: {project.Folder}")
        
        # Verify if it's the test sandbox
        folder_lower = project.Folder.lower()
        if "test_sandbox" in folder_lower:
            print("SUCCESS: The active project is correctly located in the test_sandbox directory.")
        else:
            print("WARNING: The active project is NOT in the test_sandbox directory.")
            print(f"Currently open: {project.Folder}")
            print("Please open 'tutorials/test_sandbox/Project.rmproj' in Studio RM.")
    else:
        print("ERROR: No active project found. Please load a project first.")

if __name__ == "__main__":
    main()
