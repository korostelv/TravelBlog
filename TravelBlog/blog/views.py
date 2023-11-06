from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce

from django.shortcuts import render, redirect
from .forms import PostForm, PhotoForm, CommentForm
from .models import Post, Photo, City, Comment, Like
from taggit.models import Tag
import json

from django.apps import apps

Follower = apps.get_model('registration', 'Follower')


def followers_list(user):
    if user:
        f_obj = Follower.objects.filter(user=user)
        followers = []
        for i in f_obj:
            followers.append(i.follower)
        return followers


posts = Post.objects.all()
list_used_cities = []
for p in posts:
    if p.city not in list_used_cities:
        list_used_cities.append(p.city)

profiles = User.objects.all()


@login_required
def add_post(request):
    city_list = [str(city) for city in City.objects.all()]
    city_list_json = json.dumps(city_list)

    if request.method == 'POST':
        form = PostForm(request.POST)
        files = request.FILES.getlist('image')

        city = request.POST.get('city').capitalize()
        if not City.objects.filter(name=city).exists():
            new_city = City(name=city)
            new_city.save()

        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()
            tags = form.cleaned_data['tags']
            if tags:
                f.tags.set(tags.split(','))
            f.save()
            messages.success(request, "Добавлен новый пост")
            for i in files:
                Photo.objects.create(post=f, image=i)
            return redirect('registration:profile')
        else:
            print(form.errors)
    else:
        form = PostForm()
        photoform = PhotoForm()
        return render(request, 'blog/add_post.html',
                      {'form': form, 'photoform': photoform, 'city_list_json': city_list_json})


def index(request):
    posts = Post.objects.all()
    photos = Photo.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tags = Tag.objects.all()
    context = {
        'photos': photos,
        'page_obj': page_obj,
        'tags': sorted(tags),
        'posts': posts,
        'list_used_cities': sorted(list_used_cities),
        'profiles': profiles,
    }
    if request.user.is_authenticated:
        context['followers'] = followers_list(request.user)
    return render(request, 'blog/index.html', context, )


def show_post(request, post_id):
    post = Post.objects.filter(id=post_id)
    p = Post.objects.get(id=post_id)
    photo = Photo.objects.filter(post=post_id)
    tags = Tag.objects.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_text = comment_form.cleaned_data
            print(comment_text)
            if comment_text != '':
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = p
                comment.save()
                return redirect('blog:show_post', post_id=post_id)

    comment_form = CommentForm()
    comments = Comment.objects.filter(post=post_id)
    content = {
        'user_posts': post,
        'photos': photo,
        'tags': sorted(tags),
        'list_used_cities': sorted(list_used_cities),
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'blog/show_post.html', content)


def select_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug.strip())
    posts = Post.objects.filter(tags=tag)
    photo = Photo.objects.filter(post__in=posts)
    all_tags = Tag.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'tag': tag,
        'user_posts': posts,
        'photos': photo,
        'page_obj': page_obj,
        'tags': sorted(all_tags),
        'list_used_cities': sorted(list_used_cities)
    }
    return render(request, 'blog/select_tag.html', context)


def select_city(request, city_slug):
    posts = Post.objects.filter(city=city_slug)
    photo = Photo.objects.filter(post__in=posts)
    all_tags = Tag.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user_posts': posts,
        'photos': photo,
        'page_obj': page_obj,
        'tags': sorted(all_tags),
        'list_used_cities': sorted(list_used_cities),
        'city': city_slug
    }
    return render(request, 'blog/select_city.html', context)


def select_profile(request):
    if request.method == "POST":
        prof = request.POST.get('profile')
        posts = Post.objects.filter(author__username=prof)
        photo = Photo.objects.filter(post__in=posts)
        all_tags = Tag.objects.all()
        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'user_posts': posts,
            'photos': photo,
            'page_obj': page_obj,
            'tags': sorted(all_tags),
            'list_used_cities': sorted(list_used_cities),
            'prof': prof
        }
        return render(request, 'blog/select_profile.html', context)


def select_followers(request):
    posts = Post.objects.filter(author__in=followers_list(request.user))
    photo = Photo.objects.filter(post__in=posts)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    all_tags = Tag.objects.all()
    context = {
        'tags': sorted(all_tags),
        'page_obj': page_obj,
        'photo': photo,
        'list_used_cities': sorted(list_used_cities),
    }
    if request.user.is_authenticated:
        context['followers'] = followers_list(request.user)
    return render(request, 'blog/select_followers.html', context)


def likes(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    is_user_like = Like.objects.filter(user=user, post=post).exists()
    if not is_user_like:
        Like.objects.create(post=post, user=user, like=1)
        return redirect(request.META['HTTP_REFERER'])
    messages.warning(request, 'Вы уже оценивали эту статью.')
    return redirect(request.META['HTTP_REFERER'])


def dislikes(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    is_user_like = Like.objects.filter(user=user, post=post).exists()
    if not is_user_like:
        Like.objects.create(post=post, user=user, like=-1)
        return redirect(request.META['HTTP_REFERER'])
    messages.warning(request, 'Вы уже оценивали эту статью.')
    return redirect(request.META['HTTP_REFERER'], )


def best(request):
    if request.method == 'POST':
        value = int(request.POST.get('best')[:2])
        posts = Post.objects.annotate(rating=Coalesce(Sum('like__like'), Value(0))).order_by('-rating')[:value]
        photo = Photo.objects.filter(post__in=posts)
        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        all_tags = Tag.objects.all()
        context = {
            'photos': photo,
            'page_obj': page_obj,
            'tags': sorted(all_tags),
            'list_used_cities': sorted(list_used_cities),
        }
        return render(request, 'blog/best.html', context)


def about(request):
    return render(request, 'blog/about.html')
