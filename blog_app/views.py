from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def based_page2(request):
    return render(request, 'blog_app/page2.html')


def based_page3(request):
    data = dict()
    data['tel'] = '+ 375-29-1234567'
    data['address'] = 'Minsk, Mir, 1'
    return render(request, 'blog_app/page3.html', {'data': data})


def static_page(request):
    return render(request, 'blog_app/page1.html')


def index(request):
    return HttpResponse('<h2>Главная</h2>')


def page(request):
    return HttpResponse('<h2>Страница с текстом</h2>')

