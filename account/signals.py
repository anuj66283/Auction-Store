from random import randint
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from .tasks import activation_mail

CustomUser = get_user_model()

@receiver(post_save, sender=CustomUser)
def send_verification(sender, instance=None, created=False, **kwargs):
    if created:
        code = randint(100000, 999999)
        activation_mail.delay(instance.email, code)
        instance.code = code
        instance.save()