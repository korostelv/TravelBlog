from django.contrib import admin
from .models import Post, Photo, City, Comment, Like


class PhotoInline(admin.TabularInline):
    fk_name = 'post'
    model = Photo


class PhotoAdmin(admin.ModelAdmin):
    model = Photo
    list_display = ('id', 'post', 'image')
    list_filter = ('post',)


class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [PhotoInline, ]
    list_display = ('id', 'city', 'title', 'author', 'tag_list', 'rating')
    list_filter = ('city', 'author')
    list_display_links = ['id', 'title']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['id', 'post', 'author', 'body', 'create', 'active']
    list_filter = ['post', 'author', 'active', 'create']
    list_display_links = ['id', 'body']


class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['id', 'name', 'lat_coord', 'long_coord']


class LikeAdmin(admin.ModelAdmin):
    model = Like
    list_display = ['id', 'post', 'user', 'like']


admin.site.register(Post, PostAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
