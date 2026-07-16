"""
Diagnostic script to help connect to an open Studio RM project.

Run this AFTER Studio RM is open with a project loaded.
"""

import sys
import os

# Add parent directory to path so dmstudio is importable when run from tests/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dmstudio import initialize

print("Studio RM Project Diagnostic")
print("="*50)

# Connect to Studio
oScript = initialize.studio('StudioRM')
print(f"Connected: {oScript.Caption}")
print(f"Version: {oScript.Version}")

# Check ActiveProject
project = oScript.ActiveProject
print(f"\nActiveProject: {project}")

if project is None:
    print("\n[ISSUE] ActiveProject is None!")
    print("\nPossible solutions:")
    print("1. In Studio RM, go to: Tools > Macro > Run Python Script")
    print("   This ensures the project is registered in the COM context.")
    print("\n2. Try opening the project AFTER running this script:")
    print("   - Close Studio RM")
    print("   - Run: dmstudio\\.venv\\Scripts\\python -c \"from dmstudio import initialize; initialize.studio('StudioRM')\"")
    print("   - Open Studio RM and load your project")
    print("   - Run this diagnostic again")
    print("\n3. Check if multiple Studio instances are running:")
    
    # Try to enumerate processes
    try:
        import win32com.client
        from win32com.client import GetActiveObject
        # Try to get the active object directly
        try:
            app = GetActiveObject("Datamine.StudioRM.Application")
            print(f"\n   Found via GetActiveObject: {app.Caption}")
            print(f"   ActiveProject: {app.ActiveProject}")
        except Exception as e:
            print(f"   GetActiveObject failed: {e}")
    except ImportError:
        print("   win32com not available for process enumeration")
    
    print("\n4. Alternative: Use the project file path directly")
    print("   If you know the project directory, you can change to it:")
    print("   import os")
    print("   os.chdir(r'D:\\Path\\To\\Your\\Project')")
    print("   dm_files = [f for f in os.listdir('.') if f.endswith('.dm')]")

else:
    print(f"\n[SUCCESS] Project found!")
    name = getattr(project, 'Title', None) or getattr(project, 'Name', 'Unknown')
    directory = getattr(project, 'Folder', None) or getattr(project, 'Directory', None)
    
    print(f"Name: {name}")
    print(f"Directory: {directory}")
    print(f"Files: {project.Files.Count if hasattr(project, 'Files') else 'N/A'}")
    
    # List .dm files
    import os
    if directory and os.path.exists(directory):
        os.chdir(directory)
        dm_files = [f for f in os.listdir('.') if f.endswith('.dm')]
        print(f"\n.dm files in project: {len(dm_files)}")
        for f in dm_files[:5]:
            print(f"  - {f}")
