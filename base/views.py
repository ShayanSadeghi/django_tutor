from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'front-end developers'},
    {'id': 2, 'name': 'Rust developers'},
    {'id': 2, 'name': 'Django developers'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, "home.html", context)


def room(request):
    return render(request, "room.html")
