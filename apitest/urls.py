from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('calculate/<int:number1>/<int:number2>',views.calculate,name='calculate'),
    path('get_answer/<int:identifier>',views.getIdentifier,name='getIdentifier')
]
