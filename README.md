# signal_django
#Django Project

Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.


By default, Django signals are executed **synchronously**. This means when a signal is triggered, the code connected to the signal runs in the same process and thread as the code that triggered it.

*Code Example:*
#import post_save, receiver and MyModel
#post_save which is a built-in signal provided by Django.
#The receiver decorator is used to connect a function (the signal handler) to a signal.
#This import brings in your model, MyModel, which is presumably defined in your Django app's models.


python
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal received!")
https://github.com/psarkar8585/signal_django/blob/b3e81e6603655437eaa2ef7f2fcbdc16cadd500e/myproject/myapp/signals.py#L1
![Screenshot from 2024-09-22 18-21-20](https://github.com/user-attachments/assets/96c38d99-21c7-4af6-b6a5-5147c7bc01b1)
