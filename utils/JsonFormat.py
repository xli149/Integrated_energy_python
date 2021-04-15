from app.model.Model import EnergyType


def resFormat(data) -> list:
    """
    返回结果的格式化
    :param data: 通过数据库查询出来的数据
    :return:  json
    """
    data_list = []
    for one_data in data:
        data = {
            'energy_record_id': one_data.energy_record_id,
            'energy_rec_time': one_data.energy_rec_time,
            'energy_voltage_a': one_data.energy_voltage_a,
            'energy_voltage_b': one_data.energy_voltage_b,
            'energy_tap': one_data.energy_tap,
            'energy_concentrator': one_data.energy_concentrator,
            'energy_monitoring_point': one_data.energy_monitoring_point,
            'energy_type': EnergyType.query.get(one_data.energy_type).energy_name
        }
        data_list.append(data)
    return data_list
