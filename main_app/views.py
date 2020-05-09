from django.shortcuts import render, redirect
from .models import Item
from django.views.generic.edit import CreateView, DeleteView



def home(request):
    items = Item.objects.all()
    print(items)
    return render(request, 'index.html', {'items': items})

# def add(request):
#     return render(request, 'add.html')

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'
    success_url = '/'

class ItemDelete(DeleteView):
    model = Item
    success_url = '/'