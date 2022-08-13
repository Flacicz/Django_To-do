from django.shortcuts import render

from .models import *


def index(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})
