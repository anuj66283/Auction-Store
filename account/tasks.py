from celery import shared_task
from django.core.mail import send_mail

EMAIL_USER = "anujbhattarai66283@gmail.com"

@shared_task(name="send_activation_mail")
def activation_mail(receiver, code):
    subject = "Verification code"
    message = f"Below is the 6 digit verification code donot share with anyone {code}"
    send_mail(subject, message, EMAIL_USER, [receiver])