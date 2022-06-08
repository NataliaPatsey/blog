from django.db import models
import datetime
from django.db.models import Avg, Max,Min

# Create your models here.
class Category(models.Model):
    short_name = models.CharField(max_length=20)
    about = models.CharField(max_length=50)

    def __str__(self):
        return self.short_name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=False, blank=False)
    edit_count = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)
    summary = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    user = models.ForeignKey('auth.User', default=1, on_delete=models.CASCADE, verbose_name='user')
    image = models.ImageField(upload_to='blog_app/img/',default='blog_app/img/default.jpg')

    def __str__(self):
        return self.title

    @property
    def mark_avg(self):
        if Likemark.objects.filter(article=self).exists():
            return Likemark.objects.filter(article=self).aggregate(Avg('mark'),Max('mark'),Min('mark'))['mark__avg']
        else:
            return 0

    @property
    def mark_count(self):
        if Likemark.objects.filter(article=self).exists():
            return Likemark.objects.filter(article=self).count()
        else:
            return 0

class Likemark(models.Model):
    article = models.ForeignKey(Article,  on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='user')
    mark = models.PositiveSmallIntegerField(default=5)



