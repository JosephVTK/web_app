from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/%Y/%m/", null=True, blank=True)

    def __str__(self) -> str:
        return self.user.get_username()

