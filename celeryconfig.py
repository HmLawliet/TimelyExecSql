

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
    hostname = 'yourhost' 
    username = 'root'
    password = 'yourpassword'
    database = 'yourdatabase'
    status_noexec = 0  # 不执行的状态
    status_success = 1  # 成功状态
    status_error = 2   # 错误状态
    exec_sql = 'select id,`host`,`user`,`password`,`database`,sentence from sql_review_applications where confirmed = 1 and run = 0;'
    exec_count = 10
    update_sql = 'update sql_review_applications set run = %s ,run_time= now(), run_duration= %s where id = %s ;'


class Config_Crontab:
    minute = 0  # 0分
    hour = 2  # 2点
    day_of_month = '1-31'

    
if __name__ == "__main__":

    pass