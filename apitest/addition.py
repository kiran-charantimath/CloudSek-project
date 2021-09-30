import time
from .models import Addition
def add(number1,number2,id):
    time.sleep(10)
    add_num = number1+number2
    print(add_num)
    addition_instance = Addition.objects.get(id=id)
    addition_instance.answer=add_num
    addition_instance.save()

def hook(task):
    print("Task Completed")