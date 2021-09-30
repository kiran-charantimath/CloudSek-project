from django.db import models
class Addition(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    answer = models.IntegerField(default=None,null=True)