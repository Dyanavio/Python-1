from django.urls import path, include
from main import *
from main.views import *
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
  path("", index, name="main"),
  path("create/", create, name="create"),
  path("manage/<int:id>", manage, name="manage"),
  path("search/", search, name="search"),
  path("delete/<int:id>", delete, name="delete"),
]

