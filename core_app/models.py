from django.db import models
from django.urls import reverse

# Create your models here.
class MyModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to="profile_images/")

    def get_absolute_url(self):
        return reverse("mymodel_detail", kwargs={'pk': self.id})
