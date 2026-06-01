@echo off
setlocal enabledelayedexpansion
title NET PIRATES - GLOBAL DEPLOYMENT
color 0a
cls

echo ======================================================
echo           NET PIRATES - SETUP ASSISTANT
echo ======================================================
echo.

:: 1. SPRACHWAHL
echo [?] Do you prefer English [01] or German [02]?
set /p lang_choice="> "
set "final_lang=EN"
if "%lang_choice%"=="02" set "final_lang=DE"

:: Schreibt die Sprache direkt in die config.json (einfacher String-Ersatz)
powershell -Command "(gc config.json) -replace '\"language\": \".*\"', '\"language\": \"%final_lang%\"' | Out-File -encoding ASCII config.json"

:: 2. PYTHON CHECK
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python not found. Installing via winget...
    winget install Python.Python.3.12
    echo [!] Please restart this .bat after installation.
    pause & exit
)

:: 3. DEPENDENCIES
echo [!] Checking dependencies...
pip install -r requirements.txt

echo.
echo ======================================================
echo [SUCCESS] Setup complete. 
echo Opening config.json for your personal paths...
echo ======================================================
timeout /t 2 >nul
start notepad config.json
exit