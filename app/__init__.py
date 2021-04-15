from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS
from flask_migrate import Migrate
db = SQLAlchemy()
migrate = Migrate()


# 创建工厂函数，：将app所有配置，配置到app上，然后初始化app
def create_app():
    # config_name是应用app的配置名，参数
    app = Flask(__name__)
    CORS(app, resources=r'/*')
    # 使用from_object方法，将配置参数配置到应用对象上去
    # 这里就是选择数据库是哪一个
    app.config.from_object(Config)
    # 此回调可用于初始化应用程序以用于此数据库设置
    db.init_app(app)

    migrate.init_app(app, db)
    # 将创建的蓝本绑定注册到应用实例app上
    from app.controller.api_1_0 import Api
    # 蓝图注册
    app.register_blueprint(Api)
    return app
