from django.urls import path

from . import views

#list of all supported URLS in that application
urlpatterns = [
    # views.index refers to file views.py function index
    path("", views.index, name="index"),
    path("game", views.game, name="game"),
]