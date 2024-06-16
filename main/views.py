import os
from django.shortcuts import render


def index(request):
    return render(request, os.path.join('main', 'index.html'))


def contacts(request):
    return render(request, os.path.join('main', 'contacts.html'))


def image(request):
    return render(request, os.path.join('main', 'print.html'))


def album(request):
    return render(request, os.path.join('main', 'album.html'))
