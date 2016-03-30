__author__ = '祥祥'
from django.conf.urls import url
from . import views

urlpatterns = [

    # getArticles
    url(r'^articles/getArticles$', views.getArticles),
    url(r'^articles/collectArticles$', views.collectArticles),

    # pilot

    # getUserDetail
    url(r'^pilot/getUserDetail$', views.getUserDetail),
    url(r'^pilot/getMyCollection$', views.getMyCollection),            # 获取我的收藏

    # 获取七牛token
    url(r'^pilot/getQiniuToken$', views.getQiniuToken),
    url(r'^pilot/register$', views.register),
    url(r'^pilot/login$', views.login),


]