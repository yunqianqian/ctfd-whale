#coding=utf-8
from flask_script import Manager
from app.migrate_demo import app
from flask_migrate import Migrate,MigrateCommand
from utils.exts import db
from base_class.db_class import Image, Container
from flask_apscheduler import APScheduler
from api.frp_utils import FrpUtils

def auto_clean_container():
    with app.app_context():
        FrpUtils.update_frp_redirect()
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
manager = Manager(app)

# 1. 要使用flask_migrate，必须绑定app和db
migrate = Migrate(app,db)
# 2. 把MigrateCommand命令添加到manager中
manager.add_command('db',MigrateCommand)
scheduler.add_job(id='whale-auto-clean', func=auto_clean_container, trigger="interval", seconds=5)

if __name__ == '__main__':
    manager.run()