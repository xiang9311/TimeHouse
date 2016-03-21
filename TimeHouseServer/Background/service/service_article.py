__author__ = '祥祥'

from Background.models import ArticleCulture, ArticleForeign, ArticleHistory, ArticleHuman, ArticleJoke, ArticleLiterature, ArticleNews, ArticlePhilosophy, ArticlePhoto, TextAndImage

from Background.protocol.common_pb2 import Category
from Background import constant
from Background.protocol import common_pb2
from Background import util
from . import service_user

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

Articles = [None
            , ArticleNews
            , ArticleHistory
            , ArticleLiterature
            , ArticlePhilosophy
            , ArticleForeign
            , ArticleHuman
            , ArticleCulture
            , ArticlePhoto
            , ArticleJoke]

Categorys = ['error'
             , '时事'
             , '历史'
             , '文学'
             , '哲学'
             , '外语'
             , '人物'
             , '文化'
             , '摄影'
             , '笑话']

def getArticles(userId, category, index, articles):
    """
    获取文章列表
    :param userId: 用户id
    :param category: 分类 Category
    :param index: 第几页
    :return: 包含Article的列表
    """
    if category == common_pb2.MAIN:
        # 综合返回内容
        # 目前首页返回前五个分类
        limit_every = constant.LIMIT / 5
        for i in range(1,6):
            CurrentArticle = Articles[i]
            tblArticles = CurrentArticle.objects.order_by('create_time')[limit_every * index : limit_every * (index + 1)]
            getArticlesFromTblArticles(tblArticles, articles)
    else:
        CurrentArticle = Articles[category]
        tblArticles = CurrentArticle.objects.order_by('create_time')[constant.LIMIT * index : constant.LIMIT * (index + 1)]
        getArticlesFromTblArticles(tblArticles, articles)


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


def getArticleFromTblArticle(tblArticle, article):
    """
    把表中的article转化为proto的article
    :param tblArticle:
    :return:
    """
    date2str = util.TimeUtil(util.DEFAULT_TIME_FORMAT)

    article.id = tblArticle.id
    article.readCount = tblArticle.read_count
    article.contentType = tblArticle.content_type
    article.articleType = tblArticle.article_type
    article.title = tblArticle.title
    article.subContent = tblArticle.sub_content
    article.content = tblArticle.content
    article.coverUrl = tblArticle.cover_url
    article.url = tblArticle.content_url
    article.createTime = date2str(tblArticle.create_time)

    if tblArticle.article_type == 3:
        # 图文类型 3
        getImageAndTexts(tblArticle.id, article.imageAndTexts)
    else:
        pass

    service_user.getOrganizeByUserId(tblArticle.user_id, article.organize)

    return article