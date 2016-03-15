__author__ = '祥祥'

from Background.models import User
from Background.protocol import common_pb2

def verifyUserKey(request):
    """
    验证用户key
    :param request:
    :return:
    """
    pass



def getOrganizeByUserId(userId, organize):
    """
    通过用户的id获取proto中的组织对象
    :param userId:
    :return:
    """
    user = User.objects.get(id=userId)

    organize.id = user.id
    organize.name = user.name
    organize.avatar = user.avatar

    return organize
