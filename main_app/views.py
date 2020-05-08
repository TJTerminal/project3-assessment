from django.shortcuts import render
from .models import Item



def home(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def add(request):
    return render(request, 'add.html')