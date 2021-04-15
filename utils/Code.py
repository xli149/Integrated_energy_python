class CODE:
    SUCCESS = (10000, "请求成功")
    ADD_SUCCESS = (10010, "添加数据成功")
    PARAM_IS_INVALID = (20001, "参数无效")
    PARAM_IS_BLANK = (20002, "参数为空")
    PARAM_TYPE_BIND_ERROR = (20003, "参数类型错误")
    PARAM_NOT_COMPLETE = (20004, "参数缺失")
    USER_NOT_LOGGED_IN = (30000, "用户未登陆，请先登陆")
    USER_LOGIN_ERROR = (30001, "账户或密码错误")
