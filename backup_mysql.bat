@echo off
set db_user=root
set db_password=password
set db_name=chess_clock
set backup_dir="E:\Projects\Chess-Clock\backup"
set timestamp=%date:~-4,4%-%date:~4,2%-%date:~7,2%_%time:~0,2%-%time:~3,2%-%time:~6,2%

if not exist %backup_dir% (
    mkdir %backup_dir%
)

set backup_file=%backup_dir%\%db_name%_%timestamp%.sql

"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe" -u %db_user% -p%db_password% %db_name% > %backup_file%
echo Backup completed: %backup_file%
