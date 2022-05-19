from django.shortcuts import render
from django.http import HttpResponse
from blog_app.models import Article, Category

# Create your views here.


def index(request):
    menu = Category.objects.all()
    return render(request, 'blog_app/welcome.html',{'menu': menu})

def contact(request):
    menu = Category.objects.all()
    return render(request, 'blog_app/contact.html',{'menu': menu})


def get_item_all(request):
    menu = data = Category.objects.all()
    data =Article.objects.all()
    return render(request, 'blog_app/get_item_all.html',{'data': data, 'menu': menu})


def get_item_category(request, id):
    menu = Category.objects.all()
    category = Category.objects.get(pk=id)
    data = Article.objects.filter(category_id=id)
    return render(request, 'blog_app/get_item_category.html',{'data': data,'category': category, 'menu': menu})


def page(request):
    return HttpResponse('<h2>Страница с текстом</h2>')

