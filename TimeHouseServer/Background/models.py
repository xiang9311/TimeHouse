from django.db import models

# Create your models here.
class User(models.Model):
    """
    用户, 或组织
    """
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    pw_md5 = models.CharField(max_length=70)
    wx_no = models.CharField(max_length=100)
    wb_no = models.CharField(max_length=100)
    create_time = models.DateTimeField()

class ArticleNews(models.Model):
    """
    时事
    """
    user_id = models.ForeignKey(User)
    content_type = models.IntegerField()
    article_type = models.IntegerField()
    title = models.CharField(max_length=100)
    sub_content = models.CharField(max_length=300)
    content = models.TextField()
    cover_url = models.CharField(max_length=100)
    content_url = models.CharField(max_length=200)
    read_count = models.IntegerField()
    collect_count = models.IntegerField()
    share_count = models.IntegerField()
    create_time = models.DateTimeField()

class ArticleHistory(models.Model):
    """
    历史
    """
    user_id = models.ForeignKey(User)
    content_type = models.IntegerField()
    article_type = models.IntegerField()
    title = models.CharField(max_length=100)
    sub_content = models.CharField(max_length=300)
    content = models.TextField()
    cover_url = models.CharField(max_length=100)
    content_url = models.CharField(max_length=200)
    read_count = models.IntegerField()
    collect_count = models.IntegerField()
    share_count = models.IntegerField()
    create_time = models.DateTimeField()

class ArticleLiterature(models.Model):
    """
    文化
    """
    user_id = models.ForeignKey(User)
    content_type = models.IntegerField()
    article_type = models.IntegerField()
    title = models.CharField(max_length=100)
    sub_content = models.CharField(max_length=300)
    content = models.TextField()
    cover_url = models.CharField(max_length=100)
    content_url = models.CharField(max_length=200)
    read_count = models.IntegerField()
    collect_count = models.IntegerField()
    share_count = models.IntegerField()
    create_time = models.DateTimeField()

class ArticlePhilosophy(models.Model):
    """
    哲学
    """
    user_id = models.ForeignKey(User)
    content_type = models.IntegerField()
    article_type = models.IntegerField()
    title = models.CharField(max_length=100)
    sub_content = models.CharField(max_length=300)
    content = models.TextField()
    cover_url = models.CharField(max_length=100)
    content_url = models.CharField(max_length=200)
    read_count = models.IntegerField()
    collect_count = models.IntegerField()
    share_count = models.IntegerField()
    create_time = models.DateTimeField()

class ArticleForeign(models.Model):
    """
    外文
    """
    user_id = models.ForeignKey(User)
    content_type = models.IntegerField()
    article_type = models.IntegerField()
    title = models.CharField(max_length=100)
    sub_content = models.CharField(max_length=300)
    content = models.TextField()
    cover_url = models.CharField(max_length=100)
    content_url = models.CharField(max_length=200)
    read_count = models.IntegerField()
    collect_count = models.IntegerField()
    share_count = models.IntegerField()
    create_time = models.DateTimeField()

class ArticleHuman(models.Model):
    """
    人物
    """
    user_id = models.ForeignKey(User)
    content_type = models.IntegerField()
    article_type = models.IntegerField()
    title = models.CharField(max_length=100)
    sub_content = models.CharField(max_length=300)
    content = models.TextField()
    cover_url = models.CharField(max_length=100)
    content_url = models.CharField(max_length=200)
    read_count = models.IntegerField()
    collect_count = models.IntegerField()
    share_count = models.IntegerField()
    create_time = models.DateTimeField()

class ArticleCulture(models.Model):
    """
    人物
    """
    user_id = models.ForeignKey(User)
    content_type = models.IntegerField()
    article_type = models.IntegerField()
    title = models.CharField(max_length=100)
    sub_content = models.CharField(max_length=300)
    content = models.TextField()
    cover_url = models.CharField(max_length=100)
    content_url = models.CharField(max_length=200)
    read_count = models.IntegerField()
    collect_count = models.IntegerField()
    share_count = models.IntegerField()
    create_time = models.DateTimeField()

class ArticlePhoto(models.Model):
    """
    摄影
    """
    user_id = models.ForeignKey(User)
    content_type = models.IntegerField()
    article_type = models.IntegerField()
    title = models.CharField(max_length=100)
    sub_content = models.CharField(max_length=300)
    content = models.TextField()
    cover_url = models.CharField(max_length=100)
    content_url = models.CharField(max_length=200)
    read_count = models.IntegerField()
    collect_count = models.IntegerField()
    share_count = models.IntegerField()
    create_time = models.DateTimeField()

class ArticleJoke(models.Model):
    """
    笑话
    """
    user_id = models.ForeignKey(User)
    content_type = models.IntegerField()
    article_type = models.IntegerField()
    title = models.CharField(max_length=100)
    sub_content = models.CharField(max_length=300)
    content = models.TextField()
    cover_url = models.CharField(max_length=100)
    content_url = models.CharField(max_length=200)
    read_count = models.IntegerField()
    collect_count = models.IntegerField()
    share_count = models.IntegerField()
    create_time = models.DateTimeField()

class TextAndImage(models.Model):
    articleId = models.IntegerField()
    user_id = models.ForeignKey(User)
    text = models.CharField(max_length=300)
    image = models.CharField(max_length=300)

class Collect(models.Model):
    """
    收藏
    """
    user_id = models.ForeignKey(User)
    article_id = models.IntegerField()
    collect_type = models.IntegerField()
    collect_time = models.DateTimeField()
