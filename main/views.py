from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def index(request):
	task = Task.objects.all()
	return render(request, "main/index.html", {"title": "Главная страница", "tasks": task})


def about(request):
	return render(request, "main/about.html")