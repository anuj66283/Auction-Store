import json
from datetime import timedelta

from django.dispatch import receiver
from django.db.models.signals import post_save
from django_celery_beat.models import PeriodicTask, ClockedSchedule

from .models import Product

@receiver(post_save, sender=Product)
def product_signal(sender, instance=None, created=False, **kwargs):
    if created:
        if instance.status == 'available':
            expire_date = instance.created_at+timedelta(minutes=2)

            clocked_schedule, _ = ClockedSchedule.objects.get_or_create(clocked_time=expire_date)

            PeriodicTask.objects.create(
                name=str(instance.id),
                task='add_expiry',
                clocked=clocked_schedule,
                one_off=True,
                args=json.dumps([str(instance.id)])
            )

        return 1
    
    if instance.status == "bidded" or instance.status=="expired":
        tsk = PeriodicTask.objects.get(name=str(instance.id))
        if tsk.clocked:
            tsk.clocked.delete()
        tsk.delete()

            