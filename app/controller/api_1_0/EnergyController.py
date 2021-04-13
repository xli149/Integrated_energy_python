import time

from app.controller.api_1_0 import Api
from flask import request, jsonify
from app.model.Model import EnergyType, EnergyRecord
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
        ''
    }
    return jsonify(data=data, code=200, msg='请求成功')
