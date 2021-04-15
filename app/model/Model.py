from app import db


class UserInfoRecord(db.Model):
    """
    id
    职工id
    职工姓名
    性别
    手机号
    所属部门id
    """
    __tablename__ = 'UserInfo'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(64))  # 主键
    name = db.Column(db.String(64), nullable=False)  # 姓名不能为空
    gender = db.Column(db.Enum("男", "女"), nullable=False)  # 性别 枚举 不能为空
    phone = db.Column(db.String(11))  # 手机号可以为空
    department_id = db.Column(db.Integer, nullable=False)


#
# class UserAccountRecord(db.Model):
#     """
#     id
#     职工id
#     用户名
#     密码
#     """
#     __tablename__ = 'UserAccount'
#     id = db.Column()
#
class Department(db.Model):
    """
    id
    部门名称
    """
    __tablename__ = 'Department'
    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(64), nullable=False)


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
