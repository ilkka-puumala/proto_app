from django.urls import path
from clients.views import *

urlpatterns = [
    path('', clients, name='clients'),
    path('create', create, name='clients.create'),
]