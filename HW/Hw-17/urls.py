from django.urls import path, include
from main import *
from main.views import *
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
  path("", index, name="index"),
  path("book/<int:id>", book, name="book"),
  path("reader/<int:id>", reader, name="reader"),

  path("book/create/", createBook, name="createBook"),
  path("reader/create/", createReader, name="createReader"),

  path("book/<int:bookId>/update/", updateBook, name="updateBook"),
  path("reader/<int:readerId>/update/", updateReader, name="updateReader"),

  path("book/<int:bookId>/delete/", deleteBook, name="deleteBook"),
  path("reader/<int:readerId>/delete/", deleteReader, name="deleteReader")
]
  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)