"""
集中器 代码


"""
from flask import request, jsonify
from app import db
from app.controller.api_1_0 import Api
from app.model.Model import EnergyConcentrator


@Api.route('/energy/concentrator/add')
def add_concentrator():
    """
    集线器添加
    :return:
    """
    cont_name = request.args.get('cont_name')
    cont_place = request.args.get('cont_place')
    total_concentrator = EnergyConcentrator.query.all()
    for one in total_concentrator:
        if cont_name == one.cont_name:
            return jsonify(code=20001, msg='参数无效', data='')
    new_concentrator = EnergyConcentrator(cont_name=cont_name, cont_place=cont_place)
    db.session.add(new_concentrator)
    db.session.commit()
    return jsonify(code=10010, msg='添加数据成功', data='')


@Api.route('/energy/concentrator/query')
def query_concentrator():
    total_con = EnergyConcentrator.query.all()
    data_list = []
    for one in total_con:
        data = {
            'cont_id': one.cont_id,
            'cont_name': one.cont_name,
            'cont_place': one.cont_place
        }
        data_list.append(data)
    return jsonify(code=10000, msg='请求成功', data=data_list)
