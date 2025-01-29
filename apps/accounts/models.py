from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    storage_limits = models.IntegerField(default=10)
    money = models.IntegerField(default=20000)

    def __str__(self):
        return self.username