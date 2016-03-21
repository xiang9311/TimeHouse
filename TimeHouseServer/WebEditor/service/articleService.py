__author__ = '祥祥'

from Background.models import ArticleJoke, ArticlePhoto, ArticleCulture, ArticleForeign, ArticleHistory, ArticleHuman, ArticleLiterature, ArticleNews, ArticlePhilosophy, TextAndImage
from Background.service.service_article import Articles, Categorys
from WebEditor.constant import constant

CONTENT_TYPE = ['error', '普通文章', '短文', '图文']
ARTICLE_TYPE = ['error', 'web', '普通文章', '图文']

def addImageArticle(userId, title, category, contentType, articleType, images, texts, author):
    Article = Articles[int(category)]
    article = Article()
    article.organization_id = userId
    article.content_type = int(contentType)
    article.article_type = int(articleType)
    article.title = title
    article.sub_content = ''
    article.content = ''
    article.cover_url = ''
    article.read_count = 1
    article.collect_count = 0
    article.share_count = 0
    article.create_time = constant.getDatabaseTimeNow()
    article.author_name = author
    article.save()

    for i in range(0, len(texts)):
        textAndImage = TextAndImage()
        textAndImage.articleId = article.id
        textAndImage.organization_id = userId
        textAndImage.text = texts[i]
        textAndImage.image = images[i]
        textAndImage.save()

    return True

def addTextArticle(userId, cover, title, subContent, category, contentType, articleType, content, author):
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
    article.author_name = author
    article.save()
    return True

def addWebArticle(userId, cover, title, subContent, category, contentType, articleType, content, content_url, author):
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
    article.author_name = author
    article.save()
    return True

def getArticlesByOrgId(orgId):
    """
    根据组织id获取该组织的所有已经发布的内容
    :param orgId:
    :return:{'articles':[{'id':1, 'articlename':'asdasd'}, {...}]}
    """
    articles = []
    size = len(Articles)
    for i in range(1,size):
        articles.extend(getArticlesByOrgIdAndType(orgId, i))
    return {'articles': articles}

def getArticlesByOrgIdAndType(orgId, aType):
    """
    根据组织id获取该组织的所有已经发布的内容
    :param orgId:
    :return:{'articles':[{'id':1, 'articlename':'asdasd'}, {...}]}
    """
    Article = Articles[aType]
    articles = Article.objects.filter(organization_id=orgId).order_by('create_time')
    mArticles = []
    for article in articles:
        mArticle = {}
        mArticle['id'] = article.id
        mArticle['organization_id'] = article.organization_id
        mArticle['content_type'] = CONTENT_TYPE[article.content_type]
        mArticle['article_type'] = ARTICLE_TYPE[article.article_type]
        mArticle['category'] = Categorys[aType]
        mArticle['title'] = article.title
        mArticle['sub_content'] = article.sub_content
        mArticle['content'] = article.content
        mArticle['cover_url'] =article.cover_url
        mArticle['content_url'] = article.content_url
        mArticle['read_count'] = article.read_count
        mArticle['collect_count'] = article.collect_count
        mArticle['share_count'] = article.share_count
        mArticle['create_time'] = article.create_time
        mArticles.append(mArticle)
    return mArticles
