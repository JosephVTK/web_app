from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
def upload_to(instance, filename):
    now = timezone.now()
    if instance.title:
        _, extension = filename.split('.', 1)
        location = f'documents/{instance.user.username}/{now.year}/{now.month}/{slugify(instance.title)}.{extension}'
    else:
        location = f'documents/{instance.user.username}/{now.year}/{now.month}/{filename}'
    return location

class DocumentManager(models.Manager):
    def recent(self, limit=5):
        return self.order_by('-date_created')[:limit]

class Document(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to=upload_to)

    title = models.CharField(max_length=64, blank=True)
    summary = models.TextField(blank=True)

    is_image = models.BooleanField(default=False, editable=False)

    objects = DocumentManager()

    def __str__(self) -> str:
        return self.file.name

    def get_file_name(self):
        return self.file.name.split('/')[-1]


    def save(self, *args, **kwargs):
        if not self.pk:
            file_name, file_extension = self.file.name.split('.', 1)
            image_types = ['png', 'bmp', 'jpg', 'jpeg', 'gif', 'webp']
            if file_extension in image_types:
                self.is_image = True

        return super().save(*args, **kwargs)