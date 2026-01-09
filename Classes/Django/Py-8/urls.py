from django.urls import path, include
from main import *
from main.views import *
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
  path("contacts/", getContacts, name="getContacts"), 
  path("contacts1/", getContacts1, name="getContacts"),  
  path("review/", review, name="review"),
  path("addFilm/", addFilm, name="addFilm")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)