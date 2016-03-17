__author__ = '祥祥'

from Background import models
from WebEditor.constant import constant

def addOrganization(avatar, name, password, wx_no, wb_no):

    if not checkNameUnique(name):
        return False

    organization = models.Organization()
    organization.avatar = avatar
    organization.name = name
    organization.pw_md5 = password
    organization.wx_no = wx_no
    organization.wb_no = wb_no
    organization.is_trusteeship = True
    organization.create_time = constant.getDatabaseTimeNow()
    organization.save()
    return True

def checkNameUnique(orgName):
    count = models.Organization.objects.filter(name=orgName).count()
    if count > 0:
        return False
    else:
        return True

def checkOrganizationPassword(orgName, password):
    """

    :param orgName:
    :param password:
    :return: 是否登录成功， id
    """
    organization = models.Organization.objects.filter(name=orgName)
    if (len(organization) != 1):
        return False, 0
    else:
        for o in organization:
            if o.pw_md5 == password:
                return True, o.id
            else:
                return False, 0

def getOrganizationNameById(userId):
    organization = models.Organization.objects.get(id=userId)
    if organization:
        return organization.name
    else:
        return ''