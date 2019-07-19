#!-*-coding:utf-8-*-
from celery import Celery
from celeryconfig import Config_Celery,Config_Crontab
from celery.task.schedules import crontab 
from celery.decorators import periodic_task
from celerytask import CommandHandler
from redis import Redis
import json

app = Celery()
app.config_from_object(Config_Celery)

# 定时服务
@app.task
@periodic_task(run_every=crontab(minute=Config_Crontab.minute, hour=Config_Crontab.hour, day_of_month=Config_Crontab.day_of_month))
def timing_server():
    c = CommandHandler()
    c()

if __name__ == "__main__":
    pass


