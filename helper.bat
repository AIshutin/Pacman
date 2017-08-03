@echo off
copy nul fields.sv > nul
echo 0 > sys
Pacman.exe < 1.txt
echo 1 > sys
taskkill /im Pacman.exe