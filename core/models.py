from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class User(AbstractUser):
        email = models.EmailField(unique=True)
        phone_number = models.CharField(max_length=15, blank=True, null=True)
        profile_picture = models.ImageField(
            upload_to="profile_pictures/", blank=True, null=True
        )


class Fingerprint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fingerprint_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
