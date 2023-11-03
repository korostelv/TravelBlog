# from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} '


# class Follower(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
#     follower = models.ManyToManyField(User, related_name='followers')
#
#     def __str__(self):
#         return self.user.username


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE,blank=False,default=None, related_name='followers')

    def __str__(self):
        return self.user.username


