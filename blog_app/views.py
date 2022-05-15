from django.shortcuts import render
from django.http import HttpResponse
from blog_app.models import Article, Category

# Create your views here.


def index(request):
    data = Category.objects.all()
    return render(request, 'blog_app/base.html',{'data': data})


def based_page2(request):
    return render(request, 'blog_app/page2.html')


def based_page3(request):
    data = dict()
    data['tel'] = '+ 375-29-1234567'
    data['address'] = 'Minsk, Mir, 1'
    return render(request, 'blog_app/page3.html', {'data': data})


def static_page(request):
    return render(request, 'blog_app/page1.html')





def page(request):
    return HttpResponse('<h2>Страница с текстом</h2>')

