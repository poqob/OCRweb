@echo off

REM Stop and remove all running containers
for /f "tokens=*" %%x in ('docker ps -q') do (
    docker stop %%x
    docker rm %%x
)