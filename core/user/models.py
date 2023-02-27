from django.db import models
from django.contrib.auth.models import AbstractUser


class UserBase(AbstractUser):
    coins = models.IntegerField(default=10000)
