from django.db.models.signals import post_save, pre_delete
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created or not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)

@receiver(post_save, sender=get_user_model())
def save_profile(sender, instance, **kwargs):
    instance.profile.save()