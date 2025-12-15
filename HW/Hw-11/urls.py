from django.urls import path, include
from main import *
from main.views import *

urlpatterns = [
    path('', index, name="main"),
    path('history/', history, name="history"),
    path('history/<int:year>', historyYear, name="historyYear"),
    path('cities/', citiesAll, name="citiesAll"),
    path("cities/<str:city>", citites, name="cities"),
    path("city/", city, name="city"),
    path("cities/<str:city>/<int:year>", cityYear, name="cityYear"),
    path('facts/', facts, name="facts"),



]
