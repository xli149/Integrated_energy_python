"""
监测点代码
"""


from flask import request, jsonify
from app import db
from app.controller.api_1_0 import Api
from app.model.Model import EnergyConcentrator, EnergyMonitoringPoint


@Api.route('/energy/concentrator/monitor/add')
def add_monitor():
    mp_name = request.args.get('emp_name')
    mp_place = request.args.get('mp_place')
    mp_concentrator_id = request.args.get('mp_concentrator_id', int)
    if int(mp_concentrator_id) in [i.cont_id for i in EnergyConcentrator.query.all()]:
        new_mp = EnergyMonitoringPoint(
            emp_name=mp_name,
            emp_place=mp_place,
            emp_concentrator_id=mp_concentrator_id)
        db.session.add(new_mp)
        db.session.commit()
        return jsonify(code=10010, msg='添加数据成功', data='')
    else:
        return jsonify(code=20001, msg='参数无效，无该集中器', data='')
