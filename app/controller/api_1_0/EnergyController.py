import time

from app.controller.api_1_0 import Api
from flask import request, jsonify
from app.model.Model import EnergyType, EnergyRecord, UserInfoRecord,Department
from utils.FakeData import fake_data
from app import db


@Api.route('/user/profile', methods=['POST'])
def get_profile():
    try:
        query_name = request.args.get('name')
        if query_name is None:
            return jsonify(code=20011, msg='参数为空', data={'user_profile': None})
        user_profile = UserInfoRecord.filter_by('name'==query_name).first_or_404()
        return jsonify(code=10010, msg='查询成功', data={'user_profile':user_profile})
    except Exception as e:
        return jsonify(code=20010, msg='查询失败', data=str(e))




@Api.route('/user/public_profiles', methods=['GET'])
def get_public_profiles():
    try:
        user_profiles = UserInfoRecord.query.all()
        usr_list = []
        for user_profile in user_profiles:
            department = Department.query.get(user_profile.department_id)
            department_name = department.department_name

            usr_list.append(
                {'name': user_profile.name,
                 'employee_id': user_profile.employee_id,
                 'gender': user_profile.gender,
                 'phone': user_profile.phone,
                 'department': department_name
                 }
            )

        return jsonify(code=10010, msg='查询成功', data={'user_public_profiles':usr_list})
    except Exception as e:
        return jsonify(code=20010, msg='查询失败', data=str(e))



@Api.route('/user/add', methods=['POST'])
def add_user():
    try:
        employee_id = request.args.get('employee_id')
        name = request.args.get('name')
        gender = request.args.get('gender')
        phone = request.args.get('phone')
        department_name = request.args.get('department_name')
        if employee_id is None or gender is None or department_name is None:
            return jsonify(code=20011, msg='参数为空',
                           data={'employee_id': employee_id, 'name': name,
                                 "gender": gender, "phone": phone, "department_name": department_name})
        department = Department.query.filter_by(department_name=department_name).first_or_404()

        if department is None:
            return jsonify(code=20012, msg="部门不存在", data={'employee_id': employee_id, 'name': name,
                                                          'gender': gender, 'phone': phone,
                                                          'department_name': department_name})

        user_info_record = UserInfoRecord(employee_id=employee_id, name=name, gender=gender,
                                          phone=phone, department_id= department.id)
        db.session.add(user_info_record)
        db.session.commit()
        return jsonify(code=10010, msg='用户信息添加成功', data={'employee_id': employee_id, 'name': name,
                                 'gender': gender, 'phone': phone, 'department_name': department_name})

    except Exception as e:
        return jsonify(code=20010, msg="添加失败", data={str(e)})



@Api.route('/department/add', methods=['POST'])

def add_department():
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










