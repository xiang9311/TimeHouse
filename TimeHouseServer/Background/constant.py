__author__ = '祥祥'

# 数据库查询的分页数量
LIMIT = 5

from Background.models import  ArticleForeign, ArticleHuman, ArticleJoke, ArticleDeep, ArticlePhoto

Articles = [ArticleDeep    # 默认使用news
            , ArticleDeep
            , ArticlePhoto
            , ArticleHuman
            , ArticleJoke
            , ArticleForeign]

def getToken():
    """
    获取七牛token 过期时间 一个小时
    :return:
    """
    from WebEditor.settings import getQiniuTokenWithoutKey
    return getQiniuTokenWithoutKey()