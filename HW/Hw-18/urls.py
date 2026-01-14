from django.urls import path
from main.views import *

urlpatterns = [
    path("cookie/", cookieView, name="cookie"),
    path("random/", randomNumber, name="randomNumber"),
    path("random/<int:begin>/<int:end>", randomNumberInRange, name="randomNumberInRange"),
    path("randomrange/<int:size>", randomRange, name="randomRange"),

    path("poem/", randomPoem, name="randomPoem"),
    path('poem/author/<str:author>', randomPoemAuthor, name="randomPoemAuthor"),
    path('poem/theme/<str:theme>', randomPoemTheme, name="randomPoemTheme"),
]  