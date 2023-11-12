from django.http import HttpResponseNotFound
from django.urls import reverse


def pageNotFound(request, exception):
    home_url = reverse('blog:index')
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1><p><a href="{home_url}">Перейти на главную страницу</a></p>')