

__slots__ = ['Config_Run','Config_Celery','Config_Mysql'
        ,'Config_Crontab','Config_Redis']

class Config_Run:
    worker = ' setsid celery worker -A celeryrun --loglevel=info >/dev/null 2>&1 & '
    beat = ' setsid celery beat -A celeryrun --loglevel=info >/dev/null 2>&1 & '
    monitor_beat = 'ps -ef | grep "celery beat" | grep -v grep |wc -l'
    monitor_worker = 'ps -ef | grep "celery worker" | grep -v grep |wc -l'
    monitor_defunct = 'ps -ef | grep defunct | grep -v grep | wc -l'
    kill_beat = 'ps -ef | grep "celery beat" | grep -v grep | awk \'{print $2}\' | xargs kill -15'
    kill_worker = 'ps -ef | grep "celery worker" | grep -v grep | awk \'{print $2}\' | xargs kill -15'
    kill_defunct = ' ps -ef | grep defunct | grep -v grep | awk \'{print $2}\' | xargs kill -15'



class Config_Celery:
    broker_url = 'redis://localhost/5'
    result_backend = 'redis://localhost/5'
    task_serializer = 'json'
    result_serializer = 'json'
    accept_content = ['json']
    timezone = 'Asia/Shanghai'
    enable_utc = True


class Config_Mysql:
    hostname = 'rm-wz9dawn1azrwj5789to.mysql.rds.aliyuncs.com' 
    username = 'root'
    password = 'Hello123456'
    database = 'wpwl_web_pre'
    status_success = 1  # 成功状态
    status_error = 2   # 错误状态
    timeout = 300 #执行sql语句的总的超时时间 默认300s
    exec_sql = 'select id,`host`,`user`,`password`,`database`,sentence from sql_review_applications where confirmed = 1 and run = 0;'
    exec_count = 10
    update_sql = 'update sql_review_applications set run = %s ,run_time= "%s", run_duration= %s where id = %s ;'


class Config_Crontab:
    minute = 0  # 0分
    hour = 2  # 2点
    day_of_month = '1-31'

    
if __name__ == "__main__":
    pass
