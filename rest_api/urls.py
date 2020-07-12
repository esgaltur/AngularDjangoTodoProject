# coding=utf8
from django.conf.urls import url

from .views import TodoManageView, TodoView, TodoPkGet

urlpatterns = [
    url(r'^todos/(?P<id>\d+)$', TodoManageView.as_view()),
    url(r'^todos/$', TodoView.as_view()),
    url(r'^todos/next$', TodoPkGet.as_view()),



]
