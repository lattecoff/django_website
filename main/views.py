from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from main.templates.main.forms import TaskForm

# Create your views here.
def index(request):
	task = Task.objects.all()
	return render(request, "main/index.html", {"title": "Главная страница", "tasks": task})


def about(request):
	return render(request, "main/about.html")


def create(request):
	form = TaskForm()
	context = {"form":form}

	return render(request, "main/create.html")