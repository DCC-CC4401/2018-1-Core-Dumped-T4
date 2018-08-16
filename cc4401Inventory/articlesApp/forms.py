from django.forms import ModelForm
# Models
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'state', 'description', 'image']
