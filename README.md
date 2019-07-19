# TimelyExecSql
Timing program for SQL statement execution.

The system I run the program is centos7.

You just need to modify configuration files（celeryconfig.py）, such as information about databases.

You need to initialize celery before you use it, and install it through `pip install celery`.

Of course, you are also sure that redis is installed on your system.

If redis is not installed on your system, follow these steps：
      
    yum install epel-release
    
    yum install redis
    
    systemctl enable redis-server
    
    systemctl start redis.service
    

The entry to the program is celeryapp.py. 

There are scripts that can run directly, but you are not sure if your system has execution rights. You can check the execution rights of the following files at the terminal ll. 

If there are no privileges, please `chmod +x init.sh`, `chmod +x start. sh`, `chmod +x stop. sh` to grant execution privileges to the script.
