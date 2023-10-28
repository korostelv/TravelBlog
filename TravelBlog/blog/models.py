from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from taggit.models import TaggedItem
from geopy.geocoders import Nominatim


class Post(models.Model):
    city = models.CharField(max_length=30)
    title = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField(blank=False)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title


class Photo(models.Model):
    post = models.ForeignKey('Post', null=True, blank=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blogs/%Y/%m/%d/', blank=True, null=True)
    description = models.CharField( max_length=150, blank=True)

    def __str__(self):
        return self.description


class City(models.Model):
    name = models.CharField(max_length=30, blank=False)
    lat_coord = models.FloatField(default=0.0)
    long_coord = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=City)
def coord(sender, instance, **kwargs):
    geolocator = Nominatim(user_agent="Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0")
    location = geolocator.geocode(f"{instance.name} Пермский край Россия", timeout=10)
    if location:
        instance.lat_coord = location.latitude
        instance.long_coord = location.longitude




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_author')
    body = models.TextField(max_length=3000,blank=True)
    create = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['create']

    def __str__(self):
        return f'{self.author}:{self.body}'


@receiver(post_delete, sender=TaggedItem)
def after_deleting(sender, instance, **kwargs):
    if not TaggedItem.objects.filter(tag=instance.tag).exists():
        print("Удален тег", instance.tag)
        instance.tag.delete()

