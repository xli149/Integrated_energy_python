import datetime
import random


def fake_data() -> dict:
    """
    接收时间    rec_time
    用电量      electricity_consumption
    用电途径    electricity_way
    """
    data_dict = {
        'rec_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'electricity_consumption': random.randint(1, 100),
        'electricity_way': {
            'info': {1: '室内', 2: '园区', 3: '照明'},
            'data': random.choice([1, 2, 3])
        }
    }
    return data_dict
