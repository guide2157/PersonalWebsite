from django.shortcuts import render
from django.conf.urls import url
from BasicInfo import views

app_name = "BasicInfo"

urlpatterns = [
    url(r"^$", views.landing, name="landing"),
    url(r"^index/$", views.index, name="index"),
    url(r"^about/$", views.about, name="about"),
    url(r"^gallery/$", views.gallery, name="gallery"),
]