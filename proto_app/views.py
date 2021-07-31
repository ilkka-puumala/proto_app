from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<H1>Hello World!</H1>")
