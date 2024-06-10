import os
from uuid import UUID
from celery import shared_task

from django.core.mail import send_mail

from .models import Product, ProductHistory
from bid.models import Bid

EMAIL_USER = os.getenv("EMAIL_USER")

def send_buyer(bid):
    usr_mail = bid.user.email
    send_mail("Product", "Your order has been placed", EMAIL_USER, [usr_mail])

@shared_task(name="add_expiry")
def add_expiry(pid):
    pd = Product.objects.get(pk=UUID(pid))
    bid = Bid.objects.filter(product=pid).order_by("-bid_date").first()
    if bid:
        bid.winner = True
        bid.save()
        pd.status = "bidded"
        send_buyer(bid)
        ProductHistory.objects.create(buyer=bid.user, product=pd)
    else:
        pd.status="expired"
    pd.save()
    