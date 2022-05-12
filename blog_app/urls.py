from blog_app.views import index, page, static_page, based_page2, based_page3
from django.urls import path, include

urlpatterns = [
    path('', index),
    path('page/', page),
    path('page1/', static_page, name='static_page'),
    path('page2/', based_page2, name='based_page2'),
    path('page3/', based_page3, name='based_page3'),
]
