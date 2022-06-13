from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog_app.models import Article, Category,Likemark,List,Read
from blog_app.forms import ArticleForm, SearchForm, LikemarkForm, CategoryForm
##
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.views.generic.base import View

from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required, permission_required


from django.db.models import Count

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
        #category = Category.objects.get(id = request.POST['category'])
        #article = Article.objects.create(text=request.POST['text'],title=request.POST['title'],
        #                                 summary=request.POST['summary'],category=category,
        #                                 user=request.user)
        #article.save()
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
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
    form = LikemarkForm()
    return render(request, 'blog_app/get_item_one.html', {'data': data, 'menu': menu,'form':form})

def like(request,id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        if Likemark.objects.filter(user =request.user,article=article).exists():
            Likemark.objects.filter(user =request.user,article=article).update(mark=int(request.POST['mark']))
        else:
            obj = Likemark.objects.create(user =request.user,mark=int(request.POST['mark']),article=article)
            obj.save()
    return redirect('get_item_one',id)

def unlike(request,id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        if Likemark.objects.filter(user =request.user,article=article).exists():
            Likemark.objects.filter(user =request.user,article=article).delete()

    return redirect('get_item_one',id)

def dislike(request,id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        if Likemark.objects.filter(user =request.user,article=article).exists():
            Likemark.objects.filter(user =request.user,article=article).update(mark=0)
        else:
            obj = Likemark.objects.create(user=request.user, mark=0, article=article)
            obj.save()
    return redirect('get_item_one',id)

def update_item(request, id):
    menu = Category.objects.all()
    obj = Article.objects.get(id=id)
    form = ArticleForm(instance=obj)

    if request.method == 'POST':
        #category = Category.objects.get(id=request.POST['category'])
        #Article.objects.filter(id=id).update(text=request.POST['text'],title=request.POST['title'],
        #                                 summary=request.POST['summary'],category=category,
        #                                 edit_count=obj.edit_count+1)
        form = ArticleForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            Article.objects.filter(id=id).update(edit_count = 1+obj.edit_count)
        return redirect('get_item_one',id)

    return render(request, 'blog_app/update_item.html', {'form': form, 'menu': menu})


def delete_item(request, id):
    Article.objects.get(id=id).delete()
    return redirect('get_my_items')


def add_to_list(request, id):
    article = Article.objects.get(id=id)
    if List.objects.filter(user=request.user,article=article,read__isnull=True).exists():
        obj = List.objects.get(user=request.user,article=article,read__isnull=True)
        obj.count = obj.count + 1
        obj.save()
    else:
        obj = List.objects.create(user=request.user,article=article)
        obj.save()
    return_path = request.META.get('HTTP_REFERER', '/')
    return redirect(return_path)


def delete_from_list(request, id):
    article = Article.objects.get(id=id)
    obj = List.objects.get(user=request.user,article=article,read__isnull=True)
    if obj.count > 1:
        obj.count = obj.count - 1
        obj.save()
    else:
        List.objects.get(user=request.user,article=article,read__isnull=True).delete()
    return_path = request.META.get('HTTP_REFERER', '/')
    return redirect(return_path)


def drop_from_list(request, id):
    article = Article.objects.get(id=id)
    List.objects.get(user=request.user,article=article,read__isnull=True).delete()
    return_path = request.META.get('HTTP_REFERER', '/')
    return redirect(return_path)


def do_list(request):
    read = Read.objects.create()
    List.objects.filter(user=request.user,read__isnull=True).update(read=read)
    return_path = request.META.get('HTTP_REFERER', '/')
    return redirect(return_path)


def get_past_list(request, id):
    menu = Category.objects.all()
    pastlist = Read.objects.get(id=id)
    data = List.objects.filter(read=pastlist)
    return render(request, 'blog_app/get_past_list.html', {'data': data, 'menu': menu})


def get_my_lists(request):
    menu = Category.objects.all()
    current= List.objects.filter(user=request.user,read__isnull=True)
    data = List.objects.filter(user=request.user,read__isnull=False).values('read').annotate(total=Count('id'))
    return render(request, 'blog_app/get_my_lists.html', {'data': data, 'menu': menu,'current': current})


def adm_get_group(request):
    group_lst = Group.objects.all()
    return render(request, 'blog_app/adm_get_group.html', {'group_lst': group_lst})


def adm_compound_group(request, id):
    group = Group.objects.get(id=id)
    user_dellst = list()
    user_addlst = list()
    for user in User.objects.all():
        if user.groups.filter(name=group.name).exists():
            user_dellst.append(user)
        else:
            user_addlst.append(user)
    return render(request, 'blog_app/adm_compound_group.html', {'group': group,
                                                                'user_dellst': user_dellst,
                                                                'user_addlst': user_addlst})


@login_required
@permission_required('auth.group.can_change_group',raise_exception=True)
def adm_add_to_group(request,group_id,user_id):
    group = Group.objects.get(id=group_id)
    user = User.objects.get(id=user_id)
    group.user_set.add(user)
    return_path = request.META.get('HTTP_REFERER', '/')
    return redirect(return_path)


def adm_del_from_group(request,group_id,user_id):
    group = Group.objects.get(id=group_id)
    user = User.objects.get(id=user_id)
    group.user_set.remove(user)
    return_path = request.META.get('HTTP_REFERER', '/')
    return redirect(return_path)

def adm_get_category(request):
    data = Category.objects.all()
    return render(request, 'blog_app/adm_get_category.html', {'data': data})


def adm_del_category(request, id):
    Category.objects.get(id=id).delete()
    return redirect('adm_get_category')


def adm_edit_category(request,id):
    category = Category.objects.get(id=id)
    form = CategoryForm(instance=category)
    msg = ''
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('adm_get_category')
    return render(request, 'blog_app/adm_edit_category.html', {'form': form})


def adm_add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adm_get_category')
    return render(request, 'blog_app/adm_edit_category.html', {'form': form})











