from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index2, name="index2"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
]
