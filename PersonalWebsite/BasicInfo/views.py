from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
from django.urls import reverse


def landing(request):
    if request.method == "POST":
        return HttpResponseRedirect(reverse('BasicInfo:index'))
    return render(request, "landing.html")


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def gallery(request):
    return render(request, "gallery.html")
