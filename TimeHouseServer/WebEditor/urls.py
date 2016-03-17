__author__ = '祥祥'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^editor/$', views.editor, name='editor'),

    url(r'^controller/$',views.get_ueditor_controller),

    # 发布内容
    url(r'^postContent/$', views.postContent, name='postContent'),
    url(r'^postTextContent/$', views.postTextContent, name='postTextContent'),

    # 登录
    url(r'^login/$', views.login, name='login'),

    # 注册
    url(r'^register/$', views.register, name='register'),

    # 用户详情
    url(r'^userDetail/$', views.userDetail, name='userDetail'),

    # 编辑页面
    url(r'^editorPage/$', views.editorPage, name='editorPage'),

    # 获取七牛token
    url(r'^getToken/$', views.getToken, name='getToken'),
]