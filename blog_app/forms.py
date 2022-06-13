from django.forms import ModelForm
from django import forms
from blog_app.models import Article, Likemark, Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['short_name', 'about']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'title', 'summary', 'text','image']

Mark_Type = (
    ('5','lvl80'),
    ('4','good!'),
    ('3','not too bad'),
    ('2','hm....'),
    ('1','Are you sure?'),
)

class LikemarkForm(forms.Form):
    mark = forms.ChoiceField(initial=5,choices=Mark_Type)



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










