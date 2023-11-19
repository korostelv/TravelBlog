from django.http import HttpResponseNotFound
from django.urls import reverse


def pageNotFound(request, exception):
    link = reverse('blog:index')
    return HttpResponseNotFound('<h1>Страница не найдена</h1><p><a href='+link+'>Перейдите на главную страницу</a></p>')