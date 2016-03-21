__author__ = '祥祥'

from Background.models import User, Organization
from Background.protocol import common_pb2
from Background import util

def verifyUserKey(request):
    """
    验证用户key
    :param request:
    :return:
    """
    pass



def getOrganizeById(userId, organize):
    """
    通过用户的id获取proto中的组织对象
    :param userId:
    :return:
    """
    u_organize = Organization.objects.get(id=userId)

    organize.id = u_organize.id
    organize.name = u_organize.name
    organize.avatar = util.getImageUrl200_200(u_organize.avatar)

    return organize

