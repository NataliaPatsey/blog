from blog_app.views import index, contact,get_item_category, get_item_all,\
    get_my_items, get_item_one
from django.urls import path, include

urlpatterns = [
    path('', index),
    path('contact/', contact, name='contact'),
    path('all/', get_item_all, name='get_item_all'),
    path('category/<int:id>/', get_item_category, name='get_item_category'),
    path('article/<int:id>/', get_item_one, name='get_item_one'),
    path('myarticles/', get_my_items, name='get_my_items'),
]
