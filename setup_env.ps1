#Requires -Version 5.1
# ============================================================================
# dmstudio Environment Setup Script for Windows (PowerShell)
# ============================================================================
# This script creates a Python virtual environment and installs all
# dependencies required for the dmstudio package.
#
# Requirements:
#   - Python 3.9 or later installed and in PATH
#   - Windows OS (required for pywin32 / COM automation)
#   - Active Datamine Studio license (runtime only)
#
# Usage:
#   .\setup_env.ps1
# ============================================================================

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "dmstudio Environment Setup" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python version: $pythonVersion"
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Please install Python 3.9+ from https://www.python.org/downloads/"
    Write-Host 'Ensure "Add Python to PATH" is checked during installation.'
    Read-Host "Press Enter to exit"
    exit 1
}

# Check Python version (minimum 3.9)
$versionCheck = python -c "import sys; v=sys.version_info; print('OK' if v>=(3,9) else 'FAIL')" 2>$null
if ($versionCheck -ne "OK") {
    Write-Host "ERROR: Python 3.9 or later is required." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if virtual environment already exists
if (Test-Path ".venv") {
    Write-Host "Virtual environment '.venv' already exists."
    $recreate = Read-Host "Recreate it? (y/N)"
    if ($recreate -eq "y" -or $recreate -eq "Y") {
        Write-Host "Removing existing virtual environment..."
        Remove-Item -Recurse -Force .venv
    } else {
        Write-Host "Using existing virtual environment."
    }
}

# Create virtual environment
if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment '.venv'..."
    python -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERROR: Failed to create virtual environment." -ForegroundColor Red
        Write-Host "Ensure the 'venv' module is available: python -m venv --help"
        Read-Host "Press Enter to exit"
        exit 1
    }
    Write-Host "Virtual environment created successfully."
}

# Activate virtual environment
Write-Host "Activating virtual environment..."
& .venv\Scripts\Activate.ps1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to activate virtual environment." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Upgrade pip
Write-Host "Upgrading pip..."
python -m pip install --upgrade pip

# Install requirements
Write-Host ""
Write-Host "Installing dmstudio dependencies..."
Write-Host "This may take a few minutes..."
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install dependencies." -ForegroundColor Red
    Write-Host "Check the error messages above and ensure you have internet access."
    Read-Host "Press Enter to exit"
    exit 1
}

# Install dmstudio in development mode
Write-Host ""
Write-Host "Installing dmstudio package in development mode..."
pip install -e .
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install dmstudio package." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "To activate the environment in the future, run:"
Write-Host "  .venv\Scripts\Activate.ps1" -ForegroundColor Yellow
Write-Host ""
Write-Host "To deactivate, run:"
Write-Host "  deactivate" -ForegroundColor Yellow
Write-Host ""
Write-Host "To verify installation:"
Write-Host '  python -c "from dmstudio import dmcommands; print(""OK"")"' -ForegroundColor Yellow
Write-Host ""
Read-Host "Press Enter to exit"
