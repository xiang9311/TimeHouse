__author__ = '祥祥'

from Background.models import User, Organization, Collect
from Background.protocol import common_pb2
from Background import util
from WebEditor.constant import constant

from Background.protocol import reader_pb2
from Background.service.service_article import Articles

def verifyUserKey(request):
    """
    验证用户key
    :param request:
    :return:
    """
    pass

def getOrganizeById(userId, organize):
    """
    通过用户的id获取proto中的Organization对象
    :param userId:
    :return:
    """
    u_organize = Organization.objects.get(id=userId)

    organize.id = u_organize.id
    organize.name = u_organize.name
    organize.avatar = util.getImageUrl200_200(u_organize.avatar)
    return organize

def getOrganizeDetailById(userId, organize):
    """
    通过id获取组织详情中的组织相关信息
    :param userId:
    :param organize:
    :return:
    """
    u_organize = Organization.objects.get(id=userId)

    organize.userId = u_organize.id
    organize.userName = u_organize.name
    organize.avatar = util.getImageUrl200_200(u_organize.avatar)
    organize.wx_no = u_organize.wx_no
    organize.wb_no = u_organize.wb_no
    pass

def register(phoneNumber, userName, pw, userAvatarKey):
    if not (phoneNumber and userAvatarKey and pw and userAvatarKey):
        return False

    users_use_name = User.objects.filter(name=userName)
    if users_use_name:
        # 该用户名已存在
        return False

    user = User()
    user.name = userName
    user.avatar = userAvatarKey
    user.pw_md5 = pw
    user.phone = phoneNumber
    user.create_time = constant.getDatabaseTimeNow()
    user.save()

    return True

def login(userName, pw, data):
    """
    登录
    :param userName: 用户名或者手机号
    :param pw:
    :param data: 返回的数据
    :return:
    """
    users = User.objects.filter(phone=userName)
    for user in users:
        if user.pw_md5 == pw:
            data.userId = user.id
            data.userName = user.name
            data.userAvatar = util.getImageUrl(user.avatar)
            data.phone = user.phone
            return True

    users = User.objects.filter(name=userName)
    for user in users:
        if user.pw_md5 == pw:
            data.userId = user.id
            data.userName = user.name
            data.userAvatar = util.getImageUrl(user.avatar)
            data.phone = user.phone
            return True
    return False

def collect(userId, articleId, category, optionType):

    article = Articles[category].objects.get(id=articleId)

    if not article:
        return False

    if optionType == reader_pb2.Request10003.COLLECT:

        collects = Collect.objects.filter(user_id=userId,article_id=articleId,collect_type=category)
        if not collects:
            mCollect = Collect()
            mCollect.article_id = articleId
            mCollect.user_id = userId
            mCollect.collect_type = int(category)
            mCollect.collect_time = constant.getDatabaseTimeNow()
            mCollect.organization_id = article.organization_id
            mCollect.article_title = article.title
            mCollect.article_type = article.article_type
            mCollect.save()
        else:
            return True
    else:
        # 取消收藏
        mCollect = Collect.objects.filter(article_id=articleId, user_id=userId, collect_type=int(category))
        for c in mCollect:
            c.delete()
    return True

def getMyCollects(userId, articles):
    """
    获取我的收藏
    :param userId: 我的id
    :param articles: 我的收藏
    :return:
    """

    dataToStr = util.TimeUtil(util.DEFAULT_TIME_FORMAT)

    tblCollects = Collect.objects.filter(user_id=userId)
    for tblCollect in tblCollects:
        c = articles.add()
        organization = c.organize
        c.id = tblCollect.id
        c.organize = getOrganizeById(tblCollect.organization_id, organization)
        c.title = tblCollect.article_title
        c.collectTime = dataToStr(tblCollect.collect_time)
        c.articleType = tblCollect.article_type
        c.articleId = tblCollect.article_id
    pass
