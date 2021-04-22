import time

from app.controller.api_1_0 import Api
from flask import request, jsonify, session, g
from app.model.Model import EnergyType, EnergyRecord, UserInfoRecord, Department, Role
from utils.FakeData import fake_data
from app import db


@Api.before_request
def before_request():
    g.user = None
    try:
        if 'user_id' in session:
            user_profile = UserInfoRecord.query.filter_by(id = session['user_id']).first_or_404()
            g.user = user_profile

    except Exception as e:
            print(f"Err: {e}, user does not exist")


def convert_profile_into_json_format(user_profile):
    try:
        if user_profile is None:
            return None
        department = Department.query.get(user_profile.department_id)
        department_name = department.department_name
        user_profile_format = {
            'name': user_profile.name,
            'employee_id': user_profile.employee_id,
            'gender': user_profile.gender,
            'phone': user_profile.phone,
            'department': department_name
        }
        return user_profile_format

    except Exception as e:
        print(f"err: {e}")


@Api.route('/user/profile', methods=['GET', 'POST'])
def get_profile():
    if not g.user:
        return jsonify(code=20010, msg='查询失败，请先登录')
    try:
        query_name = request.args.get('name')
        if query_name is None:
            return jsonify(code=20011, msg='参数为空', data={'user_profile': None})
        user_profile = UserInfoRecord.query.filter_by(name = query_name).first_or_404()
        user_profile = convert_profile_into_json_format(user_profile)

        return jsonify(code=10010, msg='查询成功', data={'user_profile': user_profile})
    except Exception as e:
        return jsonify(code=20010, msg='查询失败', data=str(e))


@Api.route('/user/public_profiles', methods=['GET'])
def get_public_profiles():
    if not g.user:
        return jsonify(code=20010, msg='查询失败，请先登录')
    try:
        user_profiles = UserInfoRecord.query.all()
        usr_list = []
        for user_profile in user_profiles:
            usr_list.append(convert_profile_into_json_format(user_profile))

        return jsonify(code=10010, msg='查询成功', data={'user_public_profiles': usr_list})
    except Exception as e:
        return jsonify(code=20010, msg='查询失败', data=str(e))


@Api.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            session.pop('user_id', None)
            account = request.form.get('account')
            pwd = request.form.get('pwd')
            '''
              如果数据库中用户名存在，查看用户名所关联密码是否等于登入密码。
              如果条件都满足，则存储用户id到session 返回true，否则返回
              False
            '''
            user_profile = UserInfoRecord.query.filter_by(account=account).first_or_404()
            if user_profile.pwd == pwd:
                session['user_id'] = user_profile.id
                return jsonify(code=10010, msg='登录成功', data={'user id': user_profile.id})
            else:
                return jsonify(code=20010, msg="登录失败，用户名或密码错误")

    except Exception as e:
        print(f'err:{e}')
        return jsonify(code=20010, msg="登录失败", data={'err': str(e)})


@Api.route('/user/add', methods=['POST'])
def add_user():
    if not g.user:
        return jsonify(code=20010, msg='查询失败，请先登录')
    try:
        account = request.args.get('account')
        pwd = request.args.get('pwd')
        employee_id = request.args.get('employee_id')
        name = request.args.get('name')
        gender = request.args.get('gender')
        phone = request.args.get('phone')
        department_name = request.args.get('department_name')
        if employee_id is None or gender is None or department_name is None:
            return jsonify(code=20011, msg='参数为空',
                           data={'account': account, 'pwd': pwd,'employee_id': employee_id, 'name': name,
                                 "gender": gender, "phone": phone, "department_name": department_name})
        department = Department.query.filter_by(department_name=department_name).first_or_404()

        if department is None:
            return jsonify(code=20012, msg="部门不存在", data={'account':account, 'pwd': pwd, 'employee_id': employee_id, 'name': name,
                                                          'gender': gender, 'phone': phone,
                                                          'department_name': department_name})

        user_info_record = UserInfoRecord(account=account, pwd=pwd, employee_id=employee_id, name=name, gender=gender,
                                          phone=phone, department_id=department.id)
        db.session.add(user_info_record)
        db.session.commit()
        return jsonify(code=10010, msg='用户信息添加成功', data={'account': account, 'pwd': pwd, 'employee_id': employee_id, 'name': name,
                                                         'gender': gender, 'phone': phone,
                                                         'department_name': department_name})

    except Exception as e:
        return jsonify(code=20010, msg="添加失败", data={str(e)})




@Api.route('/department/add', methods=['POST'])

def add_department():
    if not g.user:
        return jsonify(code=20010, msg='查询失败，请先登录')
    try:
        department_name = request.args.get('department_name')
        print(f"department: {department_name}")
        if department_name is None:
            return jsonify(code=20011, msg='参数为空', data={'department_name': department_name})
        new_department_name = Department(department_name=department_name)
        db.session.add(new_department_name)
        db.session.commit()
        return jsonify(code=10010, msg='添加成功', data={'department_name': department_name})
    except Exception as e:
        return jsonify(code=20010, msg='添加失败', data={str(e)})

