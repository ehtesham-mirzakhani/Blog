from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    avatar = models.CharField(max_length=20, null=True,blank=True, verbose_name="تصویر اواتار")

    class Meta:
        verbose_name='کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.username