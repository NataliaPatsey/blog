from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog_app.models import Article, Category
from blog_app.forms import ArticleForm, SearchForm
##
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.views.generic.base import View

# Create your views here.

def search(request):
    menu = Category.objects.all()
    form = SearchForm()
    data = []
    if request.method == 'POST':
        if request.POST['where'] == '1' and request.POST['count'] == '0':
            data = Article.objects.filter(title__icontains=request.POST['searchtext'])
        elif request.POST['where'] == '2' and request.POST['count'] == '0':
            data = Article.objects.filter(summary__icontains=request.POST['searchtext'])
        elif request.POST['where'] == '0' and request.POST['count'] == '1':
            data = Article.objects.filter(edit_count__gt=int(request.POST['count_edit']))
        elif request.POST['where'] == '0' and request.POST['count'] == '2':
            data = Article.objects.filter(edit_count__lt=int(request.POST['count_edit']))
        elif request.POST['where'] == '1' and request.POST['count'] == '2':
            data = Article.objects.filter(title__icontains=request.POST['searchtext'],edit_count__lt=int(request.POST['count_edit']))
        elif request.POST['where'] == '2' and request.POST['count'] == '2':
            data = Article.objects.filter(summary__icontains=request.POST['searchtext'],edit_count__lt=int(request.POST['count_edit']))
        elif request.POST['where'] == '1' and request.POST['count'] == '1':
            data = Article.objects.filter(title__icontains=request.POST['searchtext'],edit_count__gt=int(request.POST['count_edit']))
        elif request.POST['where'] == '2' and request.POST['count'] == '1':
            data = Article.objects.filter(summary__icontains=request.POST['searchtext'],edit_count__gt=int(request.POST['count_edit']))
    return render(request, 'blog_app/search.html', {'form': form, 'menu': menu, 'data':data})







class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "blog_app/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user=form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "blog_app/registration.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


def add_item(request):
    menu = Category.objects.all()
    form = ArticleForm()
    msg = ''

    if request.method == 'POST':
        category = Category.objects.get(id = request.POST['category'])
        article = Article.objects.create(text=request.POST['text'],title=request.POST['title'],
                                         summary=request.POST['summary'],category=category,
                                         user=request.user)
        article.save()
        msg = 'ok'

    return render(request, 'blog_app/add_item.html', {'form': form, 'menu': menu, 'msg': msg})


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

def get_my_items(request):
    menu = Category.objects.all()
    data = Article.objects.filter(user=request.user)
    category = {'short_name': 'My articles', 'about':'You can edit or remote it'}
    return render(request, 'blog_app/get_item_category.html', {'data': data, 'category': category, 'menu': menu})


def get_item_one(request, id):
    menu = Category.objects.all()
    data = Article.objects.get(id=id)
    return render(request, 'blog_app/get_item_one.html', {'data': data, 'menu': menu})


def update_item(request, id):
    menu = Category.objects.all()
    obj = Article.objects.get(id=id)
    form = ArticleForm(instance=obj)

    if request.method == 'POST':
        category = Category.objects.get(id=request.POST['category'])
        Article.objects.filter(id=id).update(text=request.POST['text'],title=request.POST['title'],
                                         summary=request.POST['summary'],category=category,edit_count=+1)
        return redirect('get_item_one',id)

    return render(request, 'blog_app/update_item.html', {'form': form, 'menu': menu})


def delete_item(request, id):
    Article.objects.get(id=id).delete()
    return redirect('get_my_items')




def page(request):
    return HttpResponse('<h2>Страница с текстом</h2>')








