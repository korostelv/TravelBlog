from django import forms
from .models import Post, Photo, Comment


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={'class ': 'form-input', 'placeholder': 'Введите теги, разделяя их запятыми'})
    )

    class Meta:
        model = Post
        fields = ['city', 'title', 'body', 'tags']
        labels = {'city': 'Город', 'title': 'Заголовок', 'body': 'Текст', 'tags': 'Теги'}
        widgets = {
            'city': forms.TextInput(attrs={'class ': 'form-input', 'placeholder': 'Введите название города'}),
            'title': forms.TextInput(attrs={'class ': 'form-input', 'placeholder': 'Напишите заголовок'}),
            'body': forms.Textarea(attrs={'class ': 'form-input', 'cols': 60, 'rows': 20, 'placeholder': 'Расскажите свою историю'}),
            # 'tags': forms.TextInput(attrs={'class ': 'form-input', 'placeholder': 'Введите теги, разделяя их запятыми'}),
        }


class PhotoForm(forms.ModelForm):
    image = MultipleFileField(required=False)

    class Meta:
        model = Photo
        fields = ['image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {'body': ' Написать комментарий'}
        fields = ['body']








