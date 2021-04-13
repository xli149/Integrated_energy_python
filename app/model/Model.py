from app import db


# 能源消耗记录
class EnergyRecord(db.Model):
    """
    id
    能源时间
    能源量
    能源来源
    """
    __tablename__ = 'Energy'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rec_time = db.Column(db.String(80), unique=True)
    electricity_consumption = db.Column(db.Integer)
    electricity_way = db.Column(db.Integer)


# 能源类型
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
