from app import db


# 能源消耗记录
class EnergyRecord(db.Model):
    """
    id
    时间
    A相电压
    B相电压
    能耗（总有功功率） 这个应为 集中器其下的监测点返回数据的总和
    集中器（西配电室，东配电室，南配电室，北配电室）
    检测点
    能耗类型 电/水/风
    """
    __tablename__ = 'EnergyRecord'
    energy_record_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    energy_rec_time = db.Column(db.String(80))
    energy_voltage_a = db.Column(db.Float)
    energy_voltage_b = db.Column(db.Float)
    energy_tap = db.Column(db.Integer)
    energy_concentrator = db.Column(db.Integer)
    energy_monitoring_point = db.Column(db.Integer)
    energy_type = db.Column(db.Integer)


# 能源类型  /废弃
class EnergyType(db.Model):
    """
    id
    能源名称
    能源类型

    """
    __tablename__ = 'EnergyType'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    energy_name = db.Column(db.String(10))
    energy_type = db.Column(db.String(10))


# 集中器
class EnergyConcentrator(db.Model):
    """
    集中器
    """
    __tablename__ = 'EnergyConcentrator'
    cont_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cont_name = db.Column(db.String(40), nullable=False)
    cont_place = db.Column(db.String(100), nullable=False)


# 监测点
class EnergyMonitoringPoint(db.Model):
    """
    检测点
    必须与集中器关联
    """
    __tablename__ = 'EnergyMonitoringPoint'
    emp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    emp_name = db.Column(db.String(40), nullable=False)
    emp_place = db.Column(db.String(50), nullable=False)
    emp_concentrator_id = db.Column(db.Integer, nullable=False)
