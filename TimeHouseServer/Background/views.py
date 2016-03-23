from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .service import service_article, service_user

from .protocol import common_pb2
from .protocol import reader_pb2, pilot_pb2

from . import constant
import time


# Create your views here.

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

def initCommonErrorResponse( cmdid, userid, common):
    """
    根据字段构造返回的common
    :param code:
    :param message:
    :param cmdid:
    :param userid:
    :return:
    """
    common.code = 100
    common.message = "You have found an ERROR."
    common.cmdid = cmdid
    common.timestamp = int(time.time() * 1000)
    common.userid = userid

@csrf_exempt
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
    request_common = request10001.common
    params = request10001.params

    try:
        response10001 = reader_pb2.Response10001()

        response_common = response10001.common
        data = response10001.data

        initCommonResponse(0, 'success', 10001, request_common.userid, response_common)

        articles = data.articles
        service_article.getArticles(request_common.userid, params.category, params.index, articles)

        data.maxCount = constant.LIMIT

        return HttpResponse(response10001.SerializeToString())
        # return HttpResponse(str(response10001))
    except Exception as error:
        response10001 = reader_pb2.Response10001()
        response_common = response10001.common
        initCommonErrorResponse(10001, request_common.userid, response_common)
        return HttpResponse(response10001.SerializeToString())

@csrf_exempt
def searchArticles(request):
    """
    搜索文章列表
    :param request:
    :return:
    """
    pass

@csrf_exempt
def collectArticles(request):
    """
    收藏文章
    :return:
    """
    pass

@csrf_exempt
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

@csrf_exempt
def verifyUsername(request):
    """
    验证用户名是否已经存在
    :param request:
    :return:
    """
    pass

@csrf_exempt
def register(request):
    """
    注册用户
    :param request:
    :return:
    """
    pass

@csrf_exempt
def login(request):
    """
    登录
    :param request:
    :return:
    """
    pass

@csrf_exempt
def getMyCollection(request):
    """
    获取我的收藏
    :param request:
    :return:
    """
    pass

@csrf_exempt
def updateUserInfo(request):
    """
    更新个人信息
    :param request:
    :return:
    """
    pass

@csrf_exempt
def getUserDetail(request):
    """
    获取用户详细信息
    :param requets:
    :return:
    """
    request11006 = pilot_pb2.Request11006()
    try:
        request11006.MergeFromString(request.read())
    except:
        pass
    request_common = request11006.common
    params = request11006.params

    try:
        response11006 = pilot_pb2.Response11006()

        response_common = response11006.common
        data = response11006.data

        initCommonResponse(0, 'success', 10001, request_common.userid, response_common)

        detailUser = data.detailUser
        articles = detailUser.articles
        if params.needArticles:
            service_article.getArticlesByOrgId(request_common.userid, params.orgId, articles)
        service_user.getOrganizeDetailById(params.orgId, detailUser)

        return HttpResponse(response11006.SerializeToString())
        # return HttpResponse(str(response11006))
    except Exception as error:
        response11006 = pilot_pb2.Response11006()
        response_common = response11006.common
        initCommonErrorResponse(11006, request_common.userid, response_common)
        return HttpResponse(response11006.SerializeToString())


    pass