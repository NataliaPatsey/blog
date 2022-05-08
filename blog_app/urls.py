from blog_app.views import index, page
from django.urls import path, include

urlpatterns = [
    path('',index),
    path('page/',page),
]