# from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} '


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ManyToManyField(User, related_name='followers')

    def __str__(self):
        return self.user.username


# class Contact(models.Model):
#     user_from = models.ForeignKey('auth.User',related_name='rel_from_set',on_delete=models.CASCADE)
#     user_to = models.ForeignKey('auth.User',related_name='rel_to_set',on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         indexes = [models.Index(fields=['-created']),]
#         ordering = ['-created']
#
#
# user_model = get_user_model()
# user_model.add_to_class('following',models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))
