# Upstream Handoff: Fixing Headless Spawns, Matplotlib Blocking, and Notebook Runner Diagnostics in `dmstudio-rm`

**Date:** 2026-10-27  
**Repository:** `dmstudio-rm` (`https://github.com/nazabrory/dmstudio-rm`)  
**Context:** Discovered during full execution of PTVI MRI Geostatistics notebooks (`PTVI_MRI_compositing.ipynb` / `PTVI_MRI_capping.ipynb`) on real production datasets in `ptvi-mri`.

---

## 1. Issues Discovered in `dmstudio-rm` (v2.0.0b17)

### Issue A: `attach_only=True` in `initialize.py` Still Spawns `-Embedding` Instances
- **File:** `dmstudio/initialize.py` lines 25–43
- **Behavior:**
  When `dmstudio.initialize.studio("StudioRM", attach_only=True)` is called, it executes:
  ```python
  def _scriptinit(dm_object, attach_only=True):
      if attach_only:
          try:
              return win32com.client.GetActiveObject(dm_object)
          except Exception:
              # checks psutil for studiorm.exe...
              pass
      return win32com.client.Dispatch(dm_object)
  ```
  If Datamine Studio RM is running but not registered in the Running Object Table (ROT), `GetActiveObject` raises `pywintypes.com_error: Operation unavailable`. The exception is caught, and execution unconditionally falls through to `win32com.client.Dispatch()`.
  Calling `Dispatch` launches a brand new headless background process:
  `"C:\Program Files\Datamine\StudioRM\Bin\StudioRM.exe" -Embedding`
  This consumes ~500 MB RAM per call and violates single-instance invariants.
- **Resolution:**
  If `attach_only=True`, `_scriptinit` must **never** call `Dispatch()`. If `GetActiveObject` fails and `psutil` confirms the process is running, raise a descriptive `RuntimeError` stating that Studio RM is active but not registered in ROT, or implement a window-based attachment mechanism.

---

### Issue B: `notebook_runner` Blocks Indefinitely on `plt.show()`
- **File:** `dmstudio/notebook_runner.py` inside `_execute_cells()`
- **Behavior:**
  When executing notebook cells via `exec(compiled, globals_dict)`, cells containing `plt.show()` (e.g. Cell 24 in `PTVI_MRI_compositing.ipynb`) open an OS GUI window and pause execution synchronously waiting for the user to close the window.
- **Resolution:**
  In `_execute_cells()`, before executing any notebook cells, enforce non-interactive matplotlib:
  ```python
  try:
      import matplotlib
      matplotlib.use('Agg')
      import matplotlib.pyplot as plt
      plt.ioff()
      plt.show = lambda *args, **kwargs: None
  except ImportError:
      pass
  ```

---

### Issue C: `SyntaxError` on IPython Cell Magics (`%%timer`, `%matplotlib`)
- **File:** `dmstudio/notebook_runner.py` inside `_execute_cells()`
- **Behavior:**
  Python's standard `compile(cell_code, ..., 'exec')` raises `SyntaxError: invalid syntax` whenever a cell starts with `%%timer`, `%time`, or `%matplotlib inline`.
- **Resolution:**
  Add a pre-compilation cleaner in `_execute_cells`:
  ```python
  def _clean_cell_code(cell_code: str) -> str:
      lines = cell_code.splitlines()
      cleaned = []
      for line in lines:
          stripped = line.strip()
          if stripped.startswith('%%') or stripped.startswith('%'):
              cleaned.append('# [IPython magic stripped] ' + line)
          elif stripped.startswith('!') or stripped.startswith('?'):
              cleaned.append('# [Shell/Help stripped] ' + line)
          else:
              cleaned.append(line)
      return '\n'.join(cleaned)
  ```

---

### Issue D: Windows Subprocess CP1252 Encoding & Stdout Mixing
- **File:** `dmstudio/notebook_runner.py` lines 162–195
- **Behavior:**
  1. `subprocess.run(cmd, text=True, ...)` on Windows defaults to `cp1252`, crashing with `UnicodeDecodeError` when cell stdout contains emojis (`✅`, `⚡`, `🚀`).
  2. Cell `print()` statements interleave with `json.dumps(result)` on `sys.stdout`, causing `json.loads(proc.stdout)` to fail with `JSONDecodeError` (`OUTPUT_PARSE_ERROR`).
- **Resolution:**
  1. Add `encoding='utf-8', errors='replace'` and pass `PYTHONUTF8=1` / `PYTHONIOENCODING=utf-8` in the subprocess environment.
  2. Wrap the JSON payload in unambiguous sentinels:
     ```python
     # in __main__:
     print(f"===DMSTUDIO_RUNNER_JSON_START===\n{json.dumps(result)}\n===DMSTUDIO_RUNNER_JSON_END===")
     ```
     and parse strictly between the markers.

---

## 2. Recommended Action Plan for `dmstudio-rm` Agent
1. Cut a branch `fix/notebook-runner-and-attach-guards` off `main` in `D:\Active\dmstudio-rm`.
2. Apply the above 4 fixes to `dmstudio/initialize.py` and `dmstudio/notebook_runner.py`.
3. Add unit tests in `tests/test_notebook_runner.py` asserting:
   - Magics (`%%timer`, `%matplotlib`) compile without `SyntaxError`.
   - `plt.show()` does not block in headless mode.
   - `attach_only=True` never invokes `Dispatch` to spawn a new process.
   - UTF-8 emoji output decodes cleanly without `UnicodeDecodeError`.
4. Bump version to `2.0.0b18` in `pyproject.toml` and `dmstudio/version.py`, update `CHANGELOG.md`, and publish/install editable (`pip install -e D:\Active\dmstudio-rm`).
