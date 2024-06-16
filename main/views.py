import os
from django.shortcuts import render

from main.models import Investment


def index(request):
    investments_list = Investment.objects.all()

    for item in investments_list:
        item.total = item.price * item.quantity
    context = {
        'objects_list': investments_list,
    }
    return render(request, os.path.join("main", "index.html"), context)


def contacts(request):
    return render(request, os.path.join("main", "contacts.html"))


def image(request):
    return render(request, os.path.join("main", "print.html"))


def album(request):
    return render(request, os.path.join("main", "album.html"))
