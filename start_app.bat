@echo off
REM Starter-Script für Windows

echo ========================================
echo   Zuordnungen Lern-App
echo ========================================
echo.

REM Prüfe ob Python installiert ist
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo FEHLER: Python ist nicht installiert!
    echo Bitte installiere Python von https://www.python.org
    echo.
    pause
    exit /b 1
)

echo Python ist installiert.
echo.
echo Starte App...
echo.

REM Starte die App
python zuordnungen_app.py

pause
