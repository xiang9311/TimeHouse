__author__ = '祥祥'

from Background.models import  ArticleForeign, ArticleHuman, ArticleJoke, ArticleDeep, ArticlePhoto, TextAndImage

from Background.protocol.common_pb2 import Category, ContentType
from Background import constant
from Background.protocol import common_pb2
from Background import util
from . import service_user
from Background.constant import Articles

from django.db import connection

# enum Category {
#   MAIN = 0;          // 首页
#   NEWS = 1;          // 时事
#   HISTORY = 2;       // 历史
#   LITERATURE = 3;    // 文学
#   PHILOSOPHY = 4;    // 哲学
#   FOREIGN = 5;       // 外文
#   HUMAN = 6;         // 人物
#   CULTURE = 7;       // 文化
#   PHOTO = 8;         // 摄影
#   JOKE = 9;          // 笑话
# }

# Articles = [ArticleDeep    # 默认使用news
#             , ArticleDeep
#             , ArticlePhoto
#             , ArticleHuman
#             , ArticleJoke
#             , ArticleForeign]

Categorys = ['error'
             , '深度'
             , '图说'
             , '人物'
             , '逗你开心'
             , '外语']

Categorys_dict = { 'categorys' : [{'index':1, 'category':'深度'}
                                  ,{'index':2, 'category':'图说'}
                                  ,{'index':3, 'category':'人物'}
                                  ,{'index':4, 'category':'逗你开心'}
                                  ,{'index':5, 'category':'外语'}],
                   'contentType' : [
                       {'index':1, 'type':'普通文章'},
                       {'index':0, 'type':'标题和大图'},
                       {'index':2, 'type':'短文'}
                   ]}

CategoryForProto = [
    common_pb2.MAIN
    , common_pb2.DEEP
    , common_pb2.IMAGES
    , common_pb2.PEOPLE
    , common_pb2.FORFUN
    , common_pb2.FOREIGN]

def getArticles(userId, category, index, articles):
    """
    获取文章列表
    :param userId: 用户id
    :param category: 分类 Category
    :param index: 第几页
    :return: 包含Article的列表
    """

    def dictfetchall(cursor):
        "Returns all rows from a cursor as a dict"
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]

    if category == common_pb2.MAIN:
        # 综合返回内容
        # 目前首页返回前五个分类
        limit_every = constant.LIMIT / 5
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM Background_articledeep
            UNION SELECT * FROM Background_articleforeign
            UNION SELECT * FROM Background_articlehuman
            UNION SELECT * FROM Background_articlejoke
            UNION SELECT * FROM Background_articlephoto
            ORDER BY create_time DESC
            LIMIT %s,%s""", [constant.LIMIT * index, constant.LIMIT * (index + 1)])
        row = dictfetchall(cursor)
        # for i in range(1,6):
        #     CurrentArticle = Articles[i]
        #     tblArticles = CurrentArticle.objects.order_by('create_time')[limit_every * index : limit_every * (index + 1)]
        getArticlesFromDictArticles(row, articles)
    else:
        CurrentArticle = Articles[category]
        tblArticles = CurrentArticle.objects.order_by('create_time').reverse()[constant.LIMIT * index : constant.LIMIT * (index + 1)]
        getArticlesFromTblArticles(tblArticles, articles)


def getArticlesByOrgId(userId, orgId, articles):
    """
    获取组织的文章列表
    :param userId:
    :param orgId:
    :param articles:
    :return:
    """
    for i in range(1,len(Articles)):
        CurrentArticle = Articles[i]
        tblArticles = CurrentArticle.objects.filter(organization_id=orgId).reverse().order_by('create_time')
        getArticlesFromTblArticles(tblArticles, articles)
    pass

def getImageAndTexts(article_id, imageAndTexts):
    """
    通过文章Id获取该文章下的图文内容
    :param articleId:
    :return: 包含ImageAndText的列表
    """
    tblImageAndTexts = TextAndImage.objects.filter(articleId=article_id)

    if tblImageAndTexts:
        for tblImageAndText in tblImageAndTexts:
            imageAndText = imageAndTexts.add()
            imageAndText.id = tblImageAndText.id
            imageAndText.imageUrl = tblImageAndText.image
            imageAndText.text = tblImageAndText.text


"""
以下是table转化成proto
"""

def getArticlesFromTblArticles(tblArticles, articles):
    """
    把数据库中的article转化为proto的article
    :param tblArticles:
    :return:
    """
    for tblArticle in tblArticles:
        article = articles.add()
        getArticleFromTblArticle(tblArticle, article)

    return articles


def getArticlesFromDictArticles(tblArticles, articles):
    """
    把数据库中的article转化为proto的article
    :param tblArticles:
    :return:
    """
    for tblArticle in tblArticles:
        article = articles.add()
        getArticleFromDictArticle(tblArticle, article)

    return articles

def getArticleFromDictArticle(tblArticle, article):
    """
    把表中的article转化为proto的article
    :param tblArticle:
    :return:
    """
    date2str = util.TimeUtil(util.DEFAULT_TIME_FORMAT)

    article.id = tblArticle['id']
    article.readCount = tblArticle['read_count']
    article.shareCount = tblArticle['share_count']
    article.authorName = tblArticle['author_name']
    article.contentType = tblArticle['content_type']
    article.articleType = tblArticle['article_type']
    article.title = tblArticle['title']
    article.subContent = tblArticle['sub_content']
    article.content = tblArticle['content']
    article.category = getCategory(tblArticle['category'])
    # article.coverUrl = util.getImageUrl200_200(tblArticle.cover_url)
    # 如果是显示大图，则返回完整图
    if tblArticle['content_type'] == common_pb2.BIG_IMAGE or tblArticle['article_type'] == 2: # 普通文章需要cover
        article.coverUrl = util.getImageUrl(tblArticle['cover_url'])
    else:
        article.coverUrl = util.getImageUrl200_200(tblArticle['cover_url'])

    article.url = tblArticle['content_url']
    article.createTime = date2str(tblArticle['create_time'])

    if tblArticle['article_type'] == 3:
        # 图文类型 3
        getImageAndTexts(tblArticle['id'], article.imageAndTexts)
    else:
        pass

    service_user.getOrganizeById(tblArticle['organization_id'], article.organize)

    return article



def getArticleFromTblArticle(tblArticle, article):
    """
    把表中的article转化为proto的article
    :param tblArticle:
    :return:
    """
    date2str = util.TimeUtil(util.DEFAULT_TIME_FORMAT)

    from TimeHouseServer.logger import info
    info(str(tblArticle))

    article.id = tblArticle.id
    article.readCount = tblArticle.read_count
    article.shareCount = tblArticle.share_count
    article.authorName = tblArticle.author_name
    article.contentType = tblArticle.content_type
    article.articleType = tblArticle.article_type
    article.title = tblArticle.title
    article.subContent = tblArticle.sub_content
    article.content = tblArticle.content
    article.category = getCategory(tblArticle.category)
    # article.coverUrl = util.getImageUrl200_200(tblArticle.cover_url)
    # 如果是显示大图，则返回完整图
    if tblArticle.content_type == common_pb2.BIG_IMAGE or tblArticle.article_type == 2: # 普通文章需要cover:
        article.coverUrl = util.getImageUrl(tblArticle.cover_url)
    else:
        article.coverUrl = util.getImageUrl200_200(tblArticle.cover_url)

    article.url = tblArticle.content_url
    article.createTime = date2str(tblArticle.create_time)

    if tblArticle.article_type == 3:
        # 图文类型 3
        getImageAndTexts(tblArticle.id, article.imageAndTexts)
    else:
        pass

    service_user.getOrganizeById(tblArticle.organization_id, article.organize)

    return article

def getCategory(category):
    return CategoryForProto[category]

def getArticleDetail(articleId, category, article):
    """
    通过分类和id获取proto中的Article对象
    :param articleId:
    :param category:
    :param article:
    :return:
    """
    CurrentArticle = Articles[category]
    tblArticle = CurrentArticle.objects.get(id=articleId)
    getArticleFromTblArticle(tblArticle, article)
    return True

def searchArticles(keyword, pageIndex, articles):
    limit_every = constant.LIMIT / 5
    for i in range(1,6):
        CurrentArticle = Articles[i]
        # .order_by('create_time') 不需要排序吧。。
        tblArticles = CurrentArticle.objects.filter(title__contains=keyword)[limit_every * pageIndex : limit_every * (pageIndex + 1)]
        getArticlesFromTblArticles(tblArticles, articles)
    return True

def count(articleId, category, optionType):
    """
    统计
    :param articleId:
    :param category:
    :param optionType:
    :return:
    """
    article = Articles[category].objects.get(id=articleId)

    if not article:
        return False

    if optionType == 1: # 阅读量
        article.read_count = article.read_count + 1
        pass
    elif optionType == 2: # 收藏
        article.collect_count = article.collect_count + 1
        pass
    elif optionType == 3: # 分享
        article.share_count = article.share_count + 1
        pass

    article.save()
    return True