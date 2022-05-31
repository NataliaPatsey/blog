from django.forms import ModelForm
from django import forms
from blog_app.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'title', 'summary', 'text']

# class ArticleFormSerch(ModelForm):
#     searchtext = forms.CharField(label='Search', max_length=100, initial='type here')
#     where = forms.ChoiceField(label='Where', choices=((0, "----"), (1, "Title"), (2, "Summary")))
#     count_edit = forms.IntegerField(label='Count of edit', initial=0)
#     count = forms.ChoiceField(label='Count', choices=((0, "----"), (1, "More than"), (2, "Less than")))
#
#     class Meta:
#         model = Article
#         fields = ['category']





class SearchForm(forms.Form):
    searchtext = forms.CharField(label='Search', max_length=100, initial='type here')
    where = forms.ChoiceField(label='Where',choices=((0, "----"), (1, "Title"), (2, "Summary")))
    count_edit = forms.IntegerField(label='Count of edit',initial=0)
    count = forms.ChoiceField(label='Count', choices=((0, "----"), (1, "More than"), (2, "Less than")))










