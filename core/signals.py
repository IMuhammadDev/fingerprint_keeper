from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import Fingerprint
import logging

User = get_user_model()
logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        # Logic to run when a new user is created
        send_mail(
            "Welcome to My App",
            "Thank you for registering in My App.",
            "from@example.com",
            [instance.email],
            fail_silently=False,
        )


@receiver(post_save, sender=Fingerprint)
def fingerprint_created(sender, instance, created, **kwargs):
    if created:
        # Logic to run when a new fingerprint is created
        logger.info(
            f"New fingerprint added for user {instance.user.username} (ID: {instance.user.id})"
        )
