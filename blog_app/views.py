from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h2>Главная</h2>')


def page(request):
    return HttpResponse('<h2>Страница с текстом</h2>')

