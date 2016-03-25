__author__ = '祥祥'
from django.conf.urls import url
from . import views

urlpatterns = [

    # getArticles
    url(r'^articles/getArticles$', views.getArticles),

    # pilot

    # getUserDetail
    url(r'^pilot/getUserDetail$', views.getUserDetail),

    # 获取七牛token
    url(r'^pilot/getQiniuToken$', views.getQiniuToken),
    url(r'^pilot/register$', views.register),
    url(r'^pilot/login$', views.login),

]