from app import db
from app.model.Model import UserInfoRecord, Role

from functools import wraps
from flask import session, abort


Permission_code = [0X01, 0X02]


def permission_can(current_user, permission):
    """
    检测用户是否有特定权限
    :param current_user
    :param permission
    :return:
    """
    role_id = current_user.role_id
    role = db.session.query(Role).filter_by(id=role_id).first()
    return (role.permissions & permission) == permission


def permission_required(permission):
    """
    权限认证装饰器
    :param permission:
    :return:
    """

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                current_user = UserInfoRecord.query.filter_by(id=session.get('user_id')).first()

                if not current_user and permission_can(current_user, permission):
                    abort(403)
                return f(*args, **kwargs)
            except:
                abort(403)

        return decorated_function

    return decorator