import os
from app import create_app

# 传入数据库选择，如果环境变量有FLASK_CONFIG配置则应用否则用default
app = create_app()


# shell
# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db)


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port='5000')
