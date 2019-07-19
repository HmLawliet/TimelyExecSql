import pymysql
from functools import wraps
from abc import ABCMeta, abstractmethod
import time
from celeryconfig import Config_Mysql
import logging


__slots__ = ['CommandHandler']


# 数据库装饰器  连接与关闭数据库 以及异常处理
def decorator_database(func) -> object:
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            db = pymysql.connect(Config_Mysql.hostname, Config_Mysql.username, Config_Mysql.password, Config_Mysql.database)
        except Exception as e:
            logging.error('error: mysql connect failed; lineno:[%s] --- 17' % (__file__))
            return
        cur = db.cursor()
        res = None
        kwargs['db'] = db
        kwargs['cur'] = cur
        try:
            res = func(None, kwargs)
        except Exception as e:
            logging.warning(
                'warnging: exec sql error, return None; lineno:[%s] --- 26' % (__file__))
            db.rollback()
        cur.close()
        db.close()
        return res
    return inner


# sql执行的基类
class Base_Command(metaclass=ABCMeta):

    @abstractmethod
    def get_command(self, *args, **kwargs):
        pass

    @abstractmethod
    def exec_command(self, *args, **kwargs):
        pass

def exec_result(command):
    exec_id,exec_host,exec_user,exec_passwd,exec_database,exec_sql=command
    exec_status = Config_Mysql.status_noexec
    
    try:
        db = pymysql.connect(exec_host, exec_user, exec_passwd, exec_database)
        cur=db.cursor()
    except Exception as e:
        logging.warning(
            'warnging: connect mysql error, return None; lineno:[%s] --- 53' % (__file__))
        return False,None,None,None 

    flag = True
    start_time = time.time()
    for j in range(Config_Mysql.exec_count):
        try:
            cur.execute(exec_sql)
            db.commit()
        except Exception as e:
            logging.warning(
                'warnging: exec sql error, return None; lineno:[%s] --- 64' % (__file__))
            flag = False
            pass
    if not flag: exec_status = Config_Mysql.status_error
    else: exec_status = Config_Mysql.status_success
    spend_time = time.time()-start_time 
    return True, exec_status, round(spend_time/Config_Mysql.exec_count,2), exec_id 

class Command(Base_Command):
    # 获取任务
    @decorator_database
    def get_command(self, kwargs) -> tuple:  # 返回的是mysql 查出要执行的语句
        try:
            # sql 的命令
            db = kwargs['db']
            cur = kwargs['cur']
            cur.execute(Config_Mysql.exec_sql)
            db.commit()
            res = cur.fetchall()
            return res
        except Exception as e:
            logging.warning(
                'warnging: exec sql error, return None; lineno:[%s] --- 84' % (__file__))
            raise e

    # 执行任务
    @decorator_database
    def exec_command(self, kwargs) -> None:  # 返回的是执行后的 sql信息执行时间，次数
        try:
            commands = kwargs['commands']
            db = kwargs['db']
            cur = kwargs['cur']
            # 处理 sql的执行后的信息
            for command in commands:
                r,s,t,i= exec_result(command)
                if r:
                    cur.execute(Config_Mysql.update_sql % (s, t, i))
                    db.commit()
        except Exception as e:
            logging.warning('warnging: exec sql error, return None; lineno:[%s] --- 104' % (__file__))
            raise e

# 代理执行
class CommandHandler(Command):

    def __call__(self):
        commands = self.get_command()
        if not commands or not isinstance(commands, tuple) or len(commands) == 0:
            return
        self.exec_command(commands=commands)


if __name__ == "__main__":

    print(__file__)
    pass
