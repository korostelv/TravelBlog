from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, logout
from taggit.models import Tag
from .models import Follower
from .forms import UserRegisterForm, UserEditForm
import json


from django.apps import apps
Post = apps.get_model('blog', 'Post')
Photo = apps.get_model('blog', 'Photo')
City = apps.get_model('blog', 'City')


posts = Post.objects.all()
list_used_cities = []
for p in posts:
    if p.city not in list_used_cities:
        list_used_cities.append(p.city)


@login_required
def profile(request):
    user = request.user
    user_posts = Post.objects.filter(author=user)

    cityes = City.objects.all()
    user_city = {}
    for city in cityes:
        coord = {}
        for post in user_posts:
            if city.name == post.city:
                coord['lat'] = city.lat_coord
                coord['long'] = city.long_coord
                user_city[city.name] = coord
    user_city_json = json.dumps(user_city)

    photos = Photo.objects.filter(post__in=user_posts)
    paginator = Paginator(user_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = Tag.objects.all()
    context = {
        'user_posts': user_posts,
        'photos': photos,
        'page_obj': page_obj,
        'tags': sorted(tags),
        'list_used_cities': sorted(list_used_cities),
        'user_city': user_city_json,
    }
    return render(request, 'registration/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect(reverse('registration:profile'))
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Информация о профиле обновлена.')
            return redirect('registration:profile')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'registration/edit_profile.html', {'form': form})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        messages.success(request, 'Ваш профиль успешно удален.')
        return redirect('blog:index')
    return render(request, 'registration/delete_profile.html')


@login_required
def follow(request, user_id):
    author = User.objects.get(id=user_id)
    is_following = Follower.objects.filter(user=request.user, follower=author).exists()
    if is_following:
        messages.warning(request, 'Вы уже подписаны на этого пользователя.')
    else:
        Follower.objects.create(user=request.user, follower=author)
    return redirect(request.META['HTTP_REFERER'],)


@login_required
def unfollow(request, user_id):
    author = User.objects.get(id=user_id)
    follower = Follower.objects.filter(user=request.user, follower=author)
    follower.delete()
    return redirect(request.META['HTTP_REFERER'])



