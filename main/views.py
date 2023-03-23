from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render("<h4>ДЗ по созданию нового url-адреса - выполнено</h4>")


def about(request):
	return HttpResponse("<h4>About</h4>")