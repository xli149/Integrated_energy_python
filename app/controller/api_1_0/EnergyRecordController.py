import time
from sqlalchemy import and_
from app.controller.api_1_0 import Api
from flask import request, jsonify
from app.model.Model import EnergyRecord
from utils import Echarts
from utils.FakeData import fake_data
from app import db
from utils.JsonFormat import resFormat


@Api.route('/energy/record/query/info/<energy_type_id>')
def query_one_info(energy_type_id):
    """
    查询一个类型的能源消耗
    :param energy_type_id:能源消耗类型
    :return:
    """
    energy_record_data = EnergyRecord.query.filter_by(energy_type=energy_type_id).all()
    if not energy_record_data:
        return jsonify(code=20003, msg='参数错误,无该数据', data='')

    return jsonify(code=10000, msg='请求成功', data=resFormat(energy_record_data))


@Api.route('/energy/record/query/info/time')
def query_time_info():
    """
    start_date 起始时间
    end_date 结束时间
    :return:
    """
    try:
        start_date = request.args.get('start_date', None)
        end_date = request.args.get('end_date', None)
        if start_date or end_date is None:
            return jsonify(code=20002, msg='参数为空', data='')
        energy_type = request.args.get('energy_type', EnergyRecord.electricity_way)
        record_list = db.session.query(EnergyRecord).filter(and_(EnergyRecord.rec_time.between(start_date, end_date),
                                                                 EnergyRecord.electricity_way == energy_type)).all()
        return jsonify(code=10000, msg='请求成功', data=resFormat(record_list))
    except KeyError as ke:
        return jsonify(code=20002, msg='参数为空', data=str(ke))


@Api.route('/create/data')
def create_data():
    """
    死循环模拟数据
    :return: 无返回结果！
    """
    while True:
        data = fake_data()
        if data:
            for i in data['energy_data']:
                new_energy = EnergyRecord(
                    energy_rec_time=data['rec_time'],
                    energy_voltage_a=i['energy_voltage_a'],
                    energy_voltage_b=i['energy_voltage_b'],
                    energy_tap=i['energy_tap'],
                    energy_concentrator=i['concentrator'],
                    energy_monitoring_point=i['monitor_point'],
                    energy_type=i['energy_type'])
                db.session.add(new_energy)
            db.session.commit()
            time.sleep(1)
        else:
            return '尚未添加能源类型！'


@Api.route('/energy/record/query/record/one')
def get_record_one():
    """
    测试接口
    :return:
    """
    return jsonify(code=10000, msg='请求成功', data=fake_data())


# ing
@Api.route('/energy/query/info/last')
def index(x_list=[], y_list=[]):
    """
    查询最新数据
    :return:
    """
    try:
        energy_concentrator = request.args.get('energy_concentrator')
        energy_monitoring_point = request.args.get('energy_monitoring_point')
        energy_voltage = request.args.get('energy_voltage')
        data = EnergyRecord.query.filter_by(energy_concentrator=energy_concentrator,
                                            energy_monitoring_point=energy_monitoring_point).order_by(
            db.desc(EnergyRecord.energy_record_id)).limit(20)
        data = resFormat(data)

        for i in data:
            x_list.append(i['energy_rec_time'])
            y_list.append(i['energy_voltage_' + energy_voltage])
        return jsonify(data=Echarts.Option.bar(x_list, y_list), code=10000, msg='请求成功')
    except Exception as e:
        return jsonify(data='', code=20000, msg="error msg：" + str(e))


@Api.route('/energy/record/query/info/total')
def query_total():
    """
    查询全部数据
    :return: json
    """
    try:
        data = EnergyRecord.query.all()
        return jsonify(data=resFormat(data), code=10000, msg='请求成功')
    except Exception as e:
        return jsonify(data="", code=20000, msg=str(e))
