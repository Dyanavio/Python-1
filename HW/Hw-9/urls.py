from django.urls import path, include, re_path
from main.views import *

urlpatterns = [
    path('', index, name="main"),
    re_path(r'^news/', news, name="news"),
    re_path(r'^government/', government, name="government"),
    re_path(r'^facts/', facts, name="facts"),
    re_path(r'^contacts/', contacts, name="contacts"),

    path('history/', history, name="history"),
    path('history/<str:topic>', historyTopic, name="historyTopic")

]
