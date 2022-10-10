from django.forms import ModelForm
from .models import Article, Classes, Comment


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = [
            'headline',
            'text'
        ]


class ClassCreateForm(ModelForm):
    class Meta:
        model = Classes
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
