from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': "Lets Learn Python!"},
    {'id': 2, 'name': "Lets Learn Java!"},
    {'id': 3, 'name': "FrontEnd Developer.!"},
]

def home(request):
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request, 'room.html')
