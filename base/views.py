from django.shortcuts import render

rooms = [
    {'id': 1, 'name': "Let's learn Python!"},
    {'id': 2, 'name': "JavaScript"},
    {'id': 3, 'name': "Night coding"},
    {'id': 4, 'name': "Web Development"},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html',  context)


def room(request, pk):
    return render(request, 'base/room.html')
