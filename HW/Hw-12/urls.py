from django.urls import path, include
from main import *
from main.views import *

urlpatterns= [
  path("", index, name="main"),
  path("silksong/", silksong, name="silksong"),
  path("silksong/<str:language>", silksongGlobal, name="silksongGlobal"),
  path("cars/", cars, name="cars"),
  path("cars/<str:mark>", carMark, name="cars"),
  path("weekday/<int:weekday>", weekday, name="weekday"), # Сделал с параметром, чтобы показать несколько
  path("headphones/", headphones, name="headphones")
]
