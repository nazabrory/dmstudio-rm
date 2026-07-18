# PyPI Publishing Guide for `dmstudio-rm`

This guide explains how to build, test, and publish the `dmstudio-rm` package to PyPI (Python Package Index) for the first time.

---

## 1. Local Restructuring Plan

Before publishing, we need to apply the packaging changes we agreed on:
1. **Move MCP Server:** Move `mcp_server.py` to `dmstudio/mcp_server.py`.
2. **Add Entry Point:** Expose a `main()` function in `dmstudio/mcp_server.py` that runs the FastMCP stdio server:
   ```python
   def main():
       mcp.run(transport='stdio')
   ```
3. **Configure `pyproject.toml`:**
   - Update `name = "dmstudio-rm"` under `[project]`.
   - Add the console script entry point:
     ```toml
     [project.scripts]
     dmstudio-mcp = "dmstudio.mcp_server:main"
     ```
4. **Update Docs:** Update `README.md` and `AGENTS.md` references from `python mcp_server.py` to `dmstudio-mcp`.

---

## 2. Setting Up Your PyPI Accounts

You will need accounts on both **TestPyPI** (for testing your uploads safely) and **PyPI** (the live index).

1. **Create Accounts:**
   - Register on **TestPyPI**: https://test.pypi.org/account/register/
   - Register on **PyPI**: https://pypi.org/account/register/
2. **Enable 2FA:** Both platforms require Two-Factor Authentication (2FA) to publish. Set up 2FA via an authenticator app (Google Authenticator, Duo, etc.) in your account settings.
3. **Generate API Tokens:**
   - Since PyPI no longer allows password-based uploads, go to **Account Settings** -> **API tokens** on both sites.
   - Generate a new token with "Entire account" scope (you can restrict it to the package later once it's created).
   - Save the token values somewhere secure. They start with `pypi-`.

---

## 3. How to Build & Publish (Step-by-Step)

Here are the commands you will run to package and release `dmstudio-rm`.

### Step 3.1: Build the Package Locally
In your terminal, make sure you have the build tool installed, clean previous build files, and build the source and wheel distributions:
```powershell
# 1. Install build tool
.venv\Scripts\python -m pip install --upgrade build twine

# 2. Build the package
.venv\Scripts\python -m build
```
This will create a `dist/` directory containing two files:
- `dmstudio_rm-<version>.tar.gz` (Source distribution)
- `dmstudio_rm-<version>-py3-none-any.whl` (Built wheel)

### Step 3.2: Test Installing Locally
Before uploading anywhere, you can install the wheel file locally to ensure the entry points work:
```powershell
# Install the built wheel
.venv\Scripts\python -m pip install dist/dmstudio_rm-2.0.0b4-py3-none-any.whl --force-reinstall

# Verify CLI command works (should start the MCP server or print help)
dmstudio-mcp --help
```

### Step 3.3: Publish to TestPyPI
TestPyPI is a sandbox environment. Uploading here lets you verify that the PyPI page looks right and imports successfully without affecting the real PyPI index:
```powershell
# Upload to TestPyPI
.venv\Scripts\python -m twine upload --repository testpypi dist/*
```
- **Username:** `__token__` (literal string)
- **Password:** Your TestPyPI API token (starts with `pypi-`)

After uploading, verify your package page on `https://test.pypi.org/project/dmstudio-rm/`.
You can test installing from TestPyPI in a clean environment:
```powershell
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ dmstudio-rm
```

### Step 3.4: Publish to Live PyPI
Once you've confirmed that the TestPyPI package works perfectly, publish to the real PyPI:
```powershell
# Upload to PyPI
.venv\Scripts\python -m twine upload dist/*
```
- **Username:** `__token__` (literal string)
- **Password:** Your live PyPI API token (starts with `pypi-...)
```
