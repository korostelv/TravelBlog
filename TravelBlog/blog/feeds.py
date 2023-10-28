from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse
from .models import Post


class LatestPostsFeed(Feed):
    title = "Travelblog - последние статьи"
    link = "/feeds/"
    description = "Новые статьи."

    def items(self):
        return Post.objects.order_by('-publish')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html((item.body), 30)

    def item_link(self, item):
        return reverse('blog:show_post', args=[item.id])