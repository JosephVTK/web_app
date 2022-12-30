from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

from datetime import timedelta
import uuid

# Create your models here.

class UserManager(UserManager):
    pass

class User(AbstractUser):
    is_two_factor_authenticated = models.BooleanField(default=False)
    objects = UserManager()

    def create_new_two_factor_token(self, delete=True):
        if hasattr(self, 'twofactortoken') and delete is True:
            self.twofactortoken.delete()

        self.twofactortoken = TwoFactorToken.objects.create(user=self)
        return self.twofactortoken

    def send_two_factor_authentication(self):
        if not settings.ACCOUNT_2FA:
            return
        
        self.create_new_two_factor_token()

        if settings.ACCOUNT_2FA_EMAIL:
            send_mail(
                subject='Two factor Authentication',
                message= f'Token = http://127.0.0.1:8000{reverse("account_two_factor_authenticate")}?username={self.username}&token={self.twofactortoken.token}',
                from_email='from@example.com',
                recipient_list=['to@example.com'],
                html_message= f'<a href="http://127.0.0.1:8000{reverse("account_two_factor_authenticate")}?username={self.username}&token={self.twofactortoken.token}">Click Here To Activate Your Account</a>',
                fail_silently=True
            )

class TwoFactorToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    expiry = models.DateTimeField(editable=False)

    def is_valid(self, delete=True):
        if timezone.now() < self.expiry:
            return True
        
        if delete:
            self.delete()

        return False
        

    def save(self, *args, **kwargs):
        if not self.expiry:
            current_time = timezone.now()
            delta = timedelta(minutes=5)
            self.expiry = current_time + delta

        return super().save(*args, **kwargs)
