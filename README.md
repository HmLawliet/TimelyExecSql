# TimelyExecSql
Timing program for SQL statement execution

You just need to modify configuration files（celeryconfig.py）, such as information about databases.

You need to initialize celery before you use it, and install it through `pip install celery`

The entry to the program is celeryapp.py. 

There are scripts that can run directly, but you are not sure if your system has execution rights. You can check the execution rights of the following files at the terminal ll. 

If there are no privileges, please Chmod + X start. sh, Chmod + X stop. sh to grant execution privileges to the script.
