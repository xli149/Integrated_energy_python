"""
数据库脚本配置工具
--------------------------------------------------------
如果更新数据库
    在命令行执行 以下脚本
如果当前项目有migrations文件夹
    跳过init命令
如果当前数据库model没有发生更改
    执行命令无效
---------------------------------------------------------
# 初始化迁移脚本文件夹
python manage.py db init
# 创建迁移脚本 在此你可以在迁移文件夹versions中检查脚本代码 自动迁移不一定总是正确的
python manage.py db migrate
# 确认无误 更新数据库
python manage.py db upgrade
"""

from flask_migrate import MigrateCommand
from flask_script import Manager
from main import app

manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
