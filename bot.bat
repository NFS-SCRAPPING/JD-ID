@echo off
set mypath=%cd%
cmd /k "cd /d %mypath%\venv\Scripts & activate & cd /d  %mypath% & python main.py"