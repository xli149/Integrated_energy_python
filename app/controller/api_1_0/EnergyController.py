import time

from app.controller.api_1_0 import Api
from flask import request, jsonify
from app.model.Model import EnergyType, EnergyRecord, UserInfoRecord,Department
from utils.FakeData import fake_data
from app import db


@Api.route('/insert/energy/type', methods=['GET'])
def insert_energy_type():
    try:
        energy_name = request.args.get('energy_name', None)
        energy_type = request.args.get('energy_type', None)
        if energy_name is None or energy_type is None:
            return jsonify(code=20011, msg='参数为空', data={'energy_name': energy_name, 'energy_type': energy_type})
        new_energy_type = EnergyType(energy_name=energy_name, energy_type=energy_type)
        db.session.add(new_energy_type)
        db.session.commit()
        return jsonify(code=10010, msg='添加成功', data={'energy_name': energy_name, 'energy_type': energy_type})
    except Exception as e:
        return jsonify(code=20010, msg='添加失败', data=str(e))


# @Api.route('/getAll')
# def get_user_info():


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
        department = Department.query.filter_by(department_name=department_name).first()

        user_info_record = UserInfoRecord(employee_id=employee_id, name=name, gender=gender,
                                          phone=phone, department_id= department.id)
        db.session.add(user_info_record)
        db.session.commit()
        return jsonify(code=10010, msg='用户信息添加成功', data={'employee_id': employee_id, 'name': name,
                                 'gender': gender, 'phone': phone, 'department_name': department_name})

    except Exception as e:
        return jsonify(code=20010, msg="添加失败", data={str(e)})



@Api.route('department/add', methods=['POST'])

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





@Api.route('/create/data')
def create_data():
    while True:
        data = fake_data()
        new_energy = EnergyRecord(
            rec_time=data['rec_time'],
            electricity_consumption=data['electricity_consumption'],
            electricity_way=data['electricity_way']['data'])
        db.session.add(new_energy)
        db.session.commit()
        time.sleep(1)




@Api.route('/')
def index():
    data = EnergyRecord.query.order_by(db.desc(EnergyRecord.id)).first()
    data = {
        'rec_time':data.rec_time,
    }
    return jsonify(data=data, code=200, msg='请求成功')
