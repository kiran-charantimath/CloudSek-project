from apitest import addition
from apitest.addition import add
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Addition
import time
from django_q.tasks import async_task
def index(request):
    return HttpResponse("Hi from test API",status=200)
    
def calculate(request,number1,number2):
    addition_instance = Addition.objects.create(number1=number1,number2=number2)
    async_task('apitest.addition.add', number1, number2,addition_instance.id,hook="apitest.addition.hook")
    return JsonResponse({"Unique Identifier":addition_instance.id}, status=200)

def getIdentifier(request,identifier):
    print(identifier)
    try:
        addition_instance = Addition.objects.get(id=int(identifier))
        if addition_instance.answer is None:
            return JsonResponse({"status":"Please wait."}, status=200)
        else:
            return JsonResponse({"Answer":addition_instance.answer}, status=200)
    except Addition.DoesNotExist:
        print("id doesnt exist")
        return JsonResponse({"status":"Identifier doesn't exist"}, status=404)