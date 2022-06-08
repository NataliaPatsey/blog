from django.contrib import admin
from blog_app.models import Category, Article,Likemark

# Register your models here.
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Likemark)
