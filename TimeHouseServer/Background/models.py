from django.db import models

# Create your models here.
class User(models.Model):
    """
    用户 普通用户
    """
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    pw_md5 = models.CharField(max_length=70)
    wx_no = models.CharField(max_length=100)
    wb_no = models.CharField(max_length=100)
    create_time = models.DateTimeField()

class Organization(models.Model):
    """
    组织
    """
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    pw_md5 = models.CharField(max_length=70)
    wx_no = models.CharField(max_length=100)
    wb_no = models.CharField(max_length=100)
    is_trusteeship = models.BooleanField()  # 是否是托管的组织（前期的组织一般都是托管，管理员们可以用来发内容）
    create_time = models.DateTimeField()

class OrganizationAdmin(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.CharField(max_length=100)
    pw_md5 = models.CharField(max_length=70)
    create_time = models.DateTimeField()

class ArticleDeep(models.Model):
    """
    时事
    """
    organization = models.ForeignKey(Organization)
    author_name = models.CharField(max_length=100)
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
    category = models.IntegerField()

class ArticleHistory(models.Model):
    """
    历史
    """
    organization = models.ForeignKey(Organization)
    author_name = models.CharField(max_length=100)
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
    category = models.IntegerField()

class ArticleLiterature(models.Model):
    """
    文化
    """
    organization = models.ForeignKey(Organization)
    author_name = models.CharField(max_length=100)
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
    category = models.IntegerField()

class ArticlePhilosophy(models.Model):
    """
    哲学
    """
    organization = models.ForeignKey(Organization)
    author_name = models.CharField(max_length=100)
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
    category = models.IntegerField()

class ArticleForeign(models.Model):
    """
    外文
    """
    organization = models.ForeignKey(Organization)
    author_name = models.CharField(max_length=100)
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
    category = models.IntegerField()

class ArticleHuman(models.Model):
    """
    人物
    """
    organization = models.ForeignKey(Organization)
    author_name = models.CharField(max_length=100)
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
    category = models.IntegerField()

class ArticleCulture(models.Model):
    """
    文化
    """
    organization = models.ForeignKey(Organization)
    author_name = models.CharField(max_length=100)
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
    category = models.IntegerField()

class ArticlePhoto(models.Model):
    """
    摄影
    """
    organization = models.ForeignKey(Organization)
    author_name = models.CharField(max_length=100)
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
    category = models.IntegerField()

class ArticleJoke(models.Model):
    """
    笑话
    """
    organization = models.ForeignKey(Organization)
    author_name = models.CharField(max_length=100)
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
    category = models.IntegerField()

class TextAndImage(models.Model):
    articleId = models.IntegerField()
    organization = models.ForeignKey(Organization)
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
