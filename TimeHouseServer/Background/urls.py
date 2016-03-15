__author__ = '祥祥'
from django.conf.urls import url
from . import views

urlpatterns = [
    # test
    url(r'^test$', views.test, name='test'),

    # getArticles
    url(r'^articles/getArticles', views.getArticles),

]