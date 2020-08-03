#coding:utf-8
from flask import Flask
from flask_apscheduler import APScheduler # 引入APScheduler

#任务配置类
class SchedulerConfig(object):
    JOBS = [
        {
            'id': 'test', # 任务id
            'func': '__main__:print_job', # 任务执行程序
            'args': None, # 执行程序参数
            'trigger': 'interval', # 任务执行类型，定时器
            'seconds': 5, # 任务执行时间，单位秒
        }
    ]
#定义任务执行程序
def print_job():
    print("I'm a scheduler!")
    
app = Flask(__name__)

#为实例化的flask引入定时任务配置
app.config.from_object(SchedulerConfig())

if __name__ == '__main__':
    scheduler = APScheduler()  # 实例化APScheduler
    scheduler.init_app(app)  # 把任务列表载入实例flask
    scheduler.start()  # 启动任务计划
    app.run(host="0.0.0.0", port=8888)