from django.urls import path

from main.views import index, contacts, image, album

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('print/', image),
    path('album/', album),
]
