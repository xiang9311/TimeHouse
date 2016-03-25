__author__ = '祥祥'

# 数据库查询的分页数量
LIMIT = 20


def getToken():
    """
    获取七牛token 过期时间 一个小时
    :return:
    """
    from WebEditor.settings import getQiniuTokenWithoutKey
    return getQiniuTokenWithoutKey()