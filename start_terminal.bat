@echo off
title KPOINT Polymarket Macro Alpha Terminal
echo =========================================================================
echo   KPOINT // POLYMARKET MACRO ALPHA TERMINAL (BLUE & WHITE)
echo   Institutional Prediction Market Intelligence Platform
echo   Signature: "KPOINT made this one. Not financial advice the risk is yours and yours only."
echo =========================================================================
echo.
cd /d "%~dp0"
echo [1/2] Launching default web browser to http://localhost:8080 ...
start "" "http://localhost:8080"
echo.
echo [2/2] Starting Python Macro Intelligence Server on port 8080...
python server.py
pause
