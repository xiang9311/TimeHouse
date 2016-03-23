__author__ = '祥祥'
from django.conf.urls import url
from . import views

urlpatterns = [

    # getArticles
    url(r'^articles/getArticles$', views.getArticles),

    # pilot

    # getUserDetail
    url(r'^pilot/getUserDetail$', views.getUserDetail),

]