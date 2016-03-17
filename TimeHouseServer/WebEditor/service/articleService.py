__author__ = '祥祥'

from Background.models import ArticleJoke, ArticlePhoto, ArticleCulture, ArticleForeign, ArticleHistory, ArticleHuman, ArticleLiterature, ArticleNews, ArticlePhilosophy, TextAndImage
from Background.service.service_article import Articles
from WebEditor.constant import constant

def addTextArticle(userId, cover, title, subContent, category, contentType, articleType, content):
    Article = Articles[int(category)]
    article = Article()
    article.organization_id = userId
    article.content_type = int(contentType)
    article.article_type = int(articleType)
    article.title = title
    article.sub_content = subContent
    article.content = content
    article.cover_url = cover
    article.read_count = 1
    article.collect_count = 0
    article.share_count = 0
    article.create_time = constant.getDatabaseTimeNow()
    article.save()
    return True

def addWebArticle(userId, cover, title, subContent, category, contentType, articleType, content, content_url):
    Article = Articles[int(category)]
    article = Article()
    article.organization_id = userId
    article.content_type = int(contentType)
    article.article_type = int(articleType)
    article.title = title
    article.sub_content = subContent
    article.content = content
    article.content_url = content_url
    article.cover_url = cover
    article.read_count = 1
    article.collect_count = 0
    article.share_count = 0
    article.create_time = constant.getDatabaseTimeNow()
    article.save()
    return True

