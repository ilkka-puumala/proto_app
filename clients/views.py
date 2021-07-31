from django.shortcuts import render, redirect
from .models import Clients
from .forms import ClientForm


# Create your views here.
def clients(request):
    queryset = Clients.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'clients.html', context)

def create(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ClientForm()
    
    context = {
        "form": form
    }
    return render(request, 'create.html', context)
