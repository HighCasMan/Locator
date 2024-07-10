from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    bio = models.TextField(default='не указано')
    profile_pic = models.ImageField(null=True, blank=True, upload_to="account/images/")
    facebook = models.CharField(max_length=50, default='не указан')
    twitter = models.CharField(max_length=50, default='не указан')
    instagram = models.CharField(max_length=50, default='не указан')


class Post(models.Model):
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

