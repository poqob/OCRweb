@echo off

setlocal enabledelayedexpansion

REM Son kapatılan konteynerin ID'sini al
for /f "tokens=*" %%i in ('docker ps -aq -f "status=exited" -n 1') do set container_id=%%i

REM Konteyneri yeniden başlat
docker start %container_id%
