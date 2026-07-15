"""
Quick Test Script for dmstudio
==============================

Run this to verify your dmstudio installation is working.
This does NOT require an active Datamine Studio license.
"""

import sys
import os

# Add parent directory to path so dmstudio is importable when run from tests/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print(f"Python: {sys.executable}")
print(f"Version: {sys.version}")
print()

# Test imports
print("Testing imports...")
try:
    from dmstudio import dmcommands, dmfiles, initialize, special
    from dmstudio import version
    print(f"  dmstudio version: {version.__version__}")
    print("  All imports OK")
except Exception as e:
    print(f"  FAILED: {e}")
    sys.exit(1)

# Test dmfile_def (doesn't need Studio)
print("\nTesting dmfile_def...")
try:
    file_def = special.dmfile_def()
    file_def.add_field('BHID', 'A', length=8)
    file_def.add_field('FROM', 'N')
    file_def.add_field('TO', 'N')
    file_def.add_field('AU', 'N')
    print("  dmfile_def OK")
    print(f"  Fields: {list(file_def.definition['Field Name'])}")
except Exception as e:
    print(f"  FAILED: {e}")
    sys.exit(1)

# Test DataFrame operations (doesn't need Studio)
print("\nTesting DataFrame operations...")
try:
    import pandas as pd
    df = pd.DataFrame({
        'BHID': ['DH001', 'DH002'],
        'FROM': [0.0, 5.0],
        'TO': [5.0, 10.0],
        'AU': [1.2, 3.4]
    })
    print("  DataFrame creation OK")
    print(f"  Rows: {len(df)}")
except Exception as e:
    print(f"  FAILED: {e}")
    sys.exit(1)

print("\n" + "="*50)
print("All tests passed!")
print("="*50)
print("\nTo connect to Studio RM, run:")
print("  cmd = dmcommands.init(version='StudioRM')")
print("\nSee examples/ folder for more.")
