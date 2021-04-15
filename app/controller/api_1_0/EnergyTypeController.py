from flask import request, jsonify

from app import db
from app.controller.api_1_0 import Api
from app.model.Model import EnergyType


@Api.route('/energy/type/insert', methods=['GET'])
def insert_energy_type():
	"""
	创建一个新的能源类型
	"""
	try:
		energy_name = request.args.get('energy_name', None)
		energy_type = request.args.get('energy_type', None)
		if energy_name is None or energy_type is None:
			return jsonify(code=20002, msg='参数为空', data={'energy_name': energy_name, 'energy_type': energy_type})
		if EnergyType.query.filter_by(energy_name=energy_name).first() is not None:
			return jsonify(code=20001, msg='参数重复,数据库已包含该类型！',
			               data={'energy_name': energy_name, 'energy_type': energy_type})
		new_energy_type = EnergyType(energy_name=energy_name, energy_type=energy_type)
		db.session.add(new_energy_type)
		db.session.commit()
		return jsonify(code=10010, msg='添加成功', data={'energy_name': energy_name, 'energy_type': energy_type})
	except Exception as e:
		return jsonify(code=20010, msg='添加失败', data=str(e))
