from django.urls import path

from .views import add_post, index, show_post, select_tag, select_city, about, select_profile
from .feeds import LatestPostsFeed

app_name = 'blog'


urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('add_post', add_post, name='add_post'),
    path('show_post/<int:post_id>/', show_post, name='show_post'),
    path('select_tag/<str:tag_slug>/', select_tag, name='select_tag'),
    path('select_city/<str:city_slug>/', select_city, name='select_city'),
    path('select_profile', select_profile, name='select_profile'),
    path('feeds', LatestPostsFeed(), name='feeds'),

]


