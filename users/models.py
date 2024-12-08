from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self):
        return self.username
