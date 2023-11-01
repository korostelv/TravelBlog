
from django.contrib import admin
from .models import Follower

class FollowerAdmin(admin.ModelAdmin):
    model = Follower
    list_display = ['id', 'user']
    list_display_links = ['id', 'user']


admin.site.register(Follower, FollowerAdmin)

