from blog_app.views import index, contact,get_item_category, get_item_all
from django.urls import path, include

urlpatterns = [
    path('', index),
    path('contact/', contact, name='contact'),
    path('all/', get_item_all, name='get_item_all'),
    path('category/<int:id>/', get_item_category, name='get_item_category'),
]
