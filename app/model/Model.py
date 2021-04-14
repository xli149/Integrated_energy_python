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
    employee_id = db.Column(db.String(64)) #主键
    name = db.Column(db.String(64), nullable=False) #姓名不能为空
    gender = db.Column(db.Enum("男", "女"), nullable=False) #性别 枚举 不能为空
    phone = db.Column(db.String(11)) #手机号可以为空
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
