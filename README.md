# signal_django
#Django Project

Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.


Answer: By default, Django signals are executed **synchronously**. This means when a signal is triggered, the code connected to the signal runs in the same process and thread as the code that triggered it.

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

![Screenshot from 2024-09-22 18-24-09](https://github.com/user-attachments/assets/3aecddee-f4f9-406a-b67a-0b01d817f8ad)




Question 2: Do Django signals run in the same thread as the caller?


Answer: Yes, by default, Django signals run in the **same thread** as the caller, meaning that if the signal is triggered in the main thread, the connected handler runs in that same thread.


*Code Example: *
python
from threading import current_thread
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print(f"Signal running in thread: {current_thread().name}")

When an instance of MyModel is saved, it will print the current thread name.
https://github.com/psarkar8585/signal_django/blob/08077979a7207f368e1279d8081c6faa60bb99b9/myproject/myapp/signals.py#L1



![Screenshot from 2024-09-22 18-46-24](https://github.com/user-attachments/assets/34b20234-7ed2-45ef-b74e-f7fb246ab33b)





Question 3: Do Django signals run in the same database transaction as the caller?


Answer: Yes, by default, Django signals (e.g., post_save) are run in the **same transaction** as the caller. This means if a signal handler fails or raises an exception, the database transaction will be rolled back.


*Code Example: *
python
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal in same transaction!")
    raise Exception("Rolling back transaction!")

# Saving the model will trigger the handler, but raising an exception will cause a rollback.

https://github.com/psarkar8585/signal_django/blob/5c23fbc946d82aad89185733e25934edfb7174d6/myproject/myapp/signals.py#L7
https://github.com/psarkar8585/signal_django/blob/5c23fbc946d82aad89185733e25934edfb7174d6/myproject/myapp/models.py#L4
https://github.com/psarkar8585/signal_django/blob/5c23fbc946d82aad89185733e25934edfb7174d6/myproject/myproject/settings.py#L33
![Screenshot from 2024-09-22 19-02-46](https://github.com/user-attachments/assets/32726d7f-2426-4c73-b2e9-64a3380da883)

![Screenshot from 2024-09-22 19-02-16](https://github.com/user-attachments/assets/8cb51da4-a1ba-47d4-8df9-f578c56bf481)

![Screenshot from 2024-09-22 19-01-54](https://github.com/user-attachments/assets/196342d4-7a42-4a61-90fe-d9bff232a2f3)





Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}


#Rectabgle class declear
#Rectangle class create
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    #
    def __iter__(self):
        yield f"Length: {self.length}"
        yield f"Width: {self.width}"

# Example usage
if __name__ == "__main__":
    #user input 
    a = int(input("enter 1st value : "))
    b = int(input("enter 2nd value : "))
    rect = Rectangle(a, b)
    for dimension in rect:
        print(dimension)
![Screenshot from 2024-09-22 19-38-20](https://github.com/user-attachments/assets/8983ab6a-b3b6-4f65-a4a0-a2740fd7f715)
Rectangle.py
https://github.com/psarkar8585/signal_django/blob/53b373f2be8843a692dd89b6ca8e6c4ad71c39c8/Rectangle.py#L1

