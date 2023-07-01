@echo off

REM Stop all running containers
for /f "tokens=*" %%x in ('docker ps -q') do (
    docker stop %%x
)
