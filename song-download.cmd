@echo off
set command="cd /d "%cd%"\venv\Scripts & activate & cd /d    "%cd%" & py main.py"
start "" cmd /C %command%
exit