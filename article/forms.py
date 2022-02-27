from django import forms

from article.models import ArticleModel


class CustomCreateArticleForm(forms.ModelForm):

    class Meta:
        model = ArticleModel
        fields = ('title', 'description', 'image', 'text')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название',
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            }),
            'image': forms.FileInput(attrs={
                'placeholder': 'Изображение',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
                'rows': 5,
            }),
        }
