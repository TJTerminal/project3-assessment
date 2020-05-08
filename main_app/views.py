from django.shortcuts import render



def home(request):
    return render(request, 'index.html', {'items': items})

def add(request):
    return render(request, 'add.html')