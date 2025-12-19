from django.urls import path, include
from main import *
from main.views import *
from django.views.generic import TemplateView

urlpatterns= [
  path("", index, name="index"),
  path("book/<int:id>", book, name="book"),
  path("reader/<int:id>", reader, name="reader")
]
