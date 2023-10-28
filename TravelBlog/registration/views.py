from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from taggit.models import Tag
from .forms import UserRegisterForm, LoginForm, UserEditForm


from django.apps import apps
Post = apps.get_model('blog', 'Post')
Photo = apps.get_model('blog', 'Photo')

from .geo import current_location

posts = Post.objects.all()
list_used_cities = []
for p in posts:
    if p.city not in list_used_cities:
        list_used_cities.append(p.city)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    messages.success(request, 'Вход выполнен успешно.')
                    return redirect('registration:profile')
                else:
                    messages.error(request, 'Учетная запись отключена.')
                    return redirect(request, 'registration:login', {'form': form})
            else:
                messages.error(request, 'Неверные учетные данные.')
                return redirect(request, 'registration:login', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    user_posts = Post.objects.filter(author=user)



    photos = Photo.objects.all()
    paginator = Paginator(user_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = Tag.objects.all()
    content = {
        'user_posts': user_posts,
        'photos': photos,
        'page_obj': page_obj,
        'tags': sorted(tags),
        'list_used_cities': sorted(list_used_cities),
        'current_location': current_location
    }
    return render(request, 'registration/profile.html',content)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            # return redirect(request, 'registration:profile')
            return render(request, 'registration/profile.html')
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
        return redirect(request, 'blog:index')
    return render(request, 'registration/delete_profile.html')



