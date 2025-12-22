from django.urls import path, include
from main import *
from main.views import *
from django.views.generic import TemplateView

urlpatterns= [
  path("", index, name="index"),
  path("entrance/", entrance, name="getContacts"),
  path('choice/', choice, name="choice"),
  path('shop/', shop, name="shop"),
  path('year/', year, name="year")
]
