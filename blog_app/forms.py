from django.forms import ModelForm
from blog_app.models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'title', 'summary', 'text']

