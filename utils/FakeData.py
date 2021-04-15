import datetime
import random
from app import db
from app.model.Model import EnergyType, EnergyConcentrator, EnergyMonitoringPoint


def fake_data() -> dict:
	"""
	假数据生成
	"""
	# 所有集中器
	total_energy_concentrator = EnergyConcentrator.query.all()
	electric_info_list = []

	if total_energy_concentrator:
		# 找到每一个集中器下面的所有检测点
		for one_concentrator in total_energy_concentrator:
			# 全部监测点
			total_monitor_point = EnergyMonitoringPoint.query.filter_by(
				emp_concentrator_id=one_concentrator.cont_id).all()
			for one_monitor_point in total_monitor_point:
				data = {
					'concentrator': one_concentrator.cont_name,
					'monitor_point': one_monitor_point.emp_name,
					'energy_voltage_a': random.uniform(200, 250),
					'energy_voltage_b': random.uniform(200, 250),
					'energy_tap': random.choice([i for i in range(50, 80)]),
					'energy_type': random.choice([eid.id for eid in EnergyType.query.all()])
				}
				electric_info_list.append(data)
		data_dict = {
			'rec_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
			'energy_data': electric_info_list,
		}
		return data_dict
	else:
		return False


if __name__ == '__main__':
	print(fake_data())
