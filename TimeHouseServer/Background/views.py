from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from .service import service_article

from .protocol import common_pb2
from .protocol import reader_pb2

from . import constant
import time


# Create your views here.

def test(request):
    article = common_pb2.Article()
    article.id = 123123
    article.title = 'This is title'
    return HttpResponse(article.SerializeToString())

def initCommonResponse(code, message, cmdid, userid, common):
    """
    根据字段构造返回的common
    :param code:
    :param message:
    :param cmdid:
    :param userid:
    :return:
    """
    common.code = code
    common.message = message
    common.cmdid = cmdid
    common.timestamp = int(time.time() * 1000)
    common.userid = userid

def getArticles(request):
    """
    获取文章列表
    :return:
    """

    # 解析成对象
    request10001 = reader_pb2.Request10001()
    try:
        request10001.MergeFromString(request.read())
    except:
        pass

    common = request10001.common
    params = request10001.params

    articles = None

    try:

        response10001 = reader_pb2.Response10001()

        common = response10001.common
        data = response10001.data

        initCommonResponse(0, 'success', 10001, common.userid, common)

        articles = data.articles
        service_article.getArticles(common.userid, params.category, params.index, articles)

        data.maxCount = constant.LIMIT

        # return HttpResponse(response10001.SerializeToString())
        return HttpResponse(str(response10001))
    except Exception as error:
        return HttpResponse("error : " + str(error.args))
        pass

def searchArticles(request):
    """
    搜索文章列表
    :param request:
    :return:
    """
    pass

def collectArticles(request):
    """
    收藏文章
    :return:
    """
    pass

def getDetailArticles(request):
    """
    获取文章详情
    :param request:
    :return:
    """
    pass



"""
用户相关
"""

def verifyUsername(request):
    """
    验证用户名是否已经存在
    :param request:
    :return:
    """
    pass

def register(request):
    """
    注册用户
    :param request:
    :return:
    """
    pass

def login(request):
    """
    登录
    :param request:
    :return:
    """
    pass

def getMyCollection(request):
    """
    获取我的收藏
    :param request:
    :return:
    """
    pass

def updateUserInfo(request):
    """
    更新个人信息
    :param request:
    :return:
    """
    pass

def getUserDetail(request):
    """
    获取用户详细信息
    :param requets:
    :return:
    """
    pass