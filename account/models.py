from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.

class UserManager(UserManager):
    pass

class User(AbstractUser):
    objects = UserManager()
