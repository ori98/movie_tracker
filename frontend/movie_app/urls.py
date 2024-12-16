from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("insert", views.insert, name="movie_insert"),
    path("browse", views.browse, name="movie_browse")
]