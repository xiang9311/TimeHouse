__author__ = '祥祥'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^editor/$', views.editor, name='editor'),

    url(r'^controller/$',views.get_ueditor_controller),
]