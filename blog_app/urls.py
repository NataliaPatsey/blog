from blog_app.views import index, contact,get_item_category,get_item_all,\
    get_my_items, get_item_one,add_item,RegisterFormView, LoginFormView,LogoutView, update_item,\
    delete_item, search

from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('all/', get_item_all, name='get_item_all'),
    path('category/<int:id>/', get_item_category, name='get_item_category'),
    path('article/<int:id>/', get_item_one, name='get_item_one'),
    path('editarticle/<int:id>/', update_item, name='update_item'),
    path('delarticles/<int:id>/', delete_item, name='delete_item'),
    path('addarticle/', add_item, name='add_item'),
    path('myarticles/', get_my_items, name='get_my_items'),
    path('search/', search, name='search'),

    path('registration/', RegisterFormView.as_view(), name='registration'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

