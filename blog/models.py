from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Tag(models.Model):
    identifier = models.CharField(max_length=32, primary_key=True)

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={ 'pk': self.identifier })

    def __str__(self) -> str:
        return self.identifier

class Article(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)

    date_created = models.DateField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    is_published = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={ 'slug': self.slug })

    def __str__(self) -> str:
        return self.title