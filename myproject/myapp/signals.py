from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, created, **kwargs):
    if created:
        print(f"Signal received! A new instance of MyModel was created: {instance.name}")
