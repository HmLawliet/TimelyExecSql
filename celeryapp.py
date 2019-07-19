import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import time 
import logging
from celeryconfig import Config_Run
import threading


# 初始化日志
def initlogger() -> object:
    '''
    初始化日志配置
    '''
    # 第一步，创建一个logger
    logging.basicConfig()
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)  # Log等级总开关
    # 第二步，创建一个handler，用于写入日志文件
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    log_path = os.path.dirname(os.getcwd()) + '/CeleryLogs/'
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_name = log_path + rq + '.log'
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.WARNING)  # 输出到file的log等级的开关
    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)
    return logger

def run_worker():
    os.system(Config_Run.worker)
    logging.info("worker 启动成功！")

def run_beat():
    os.system(Config_Run.beat)
    logging.info("beat 启动成功！")

def run() -> None:
    threading.Thread(target=run_worker).start()
    threading.Thread(target=run_beat).start()
    

def monitor() -> bool:
    worker_count = int(os.popen(Config_Run.monitor_worker).read().strip())
    beat_count = int(os.popen(Config_Run.monitor_beat).read().strip()) 
    return True if (worker_count>0 and beat_count>0) else False

def kill() -> None:
    if int(os.popen(Config_Run.monitor_worker).read().strip()) > 0:
        os.system(Config_Run.kill_worker)
    if int(os.popen(Config_Run.monitor_beat).read().strip()) > 0:
        os.system(Config_Run.kill_beat)
    if int(os.popen(Config_Run.monitor_defunct).read().strip()) > 0:
        os.system(Config_Run.kill_defunct)
    time.sleep(2) 
    

# 启动  监控
# beat worker 分别启动

class App:
    def app(self) -> None:
        initlogger() # 初始化日志
        logging.info("启动定时执行sql任务")
        while True:
            if not monitor():
                kill()
                run() 
            time.sleep(3600)
    
    def __del__(self) -> None:
        kill()

if __name__ == "__main__":
    App().app()
    pass