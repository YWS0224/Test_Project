from django.db import models
from type.models import *


# Create your models here.

class goods(models.Model):
    goodName = models.CharField(max_length=30)
    goodNum = models.IntegerField()
    goodPrice = models.FloatField()
    goodType = models.ForeignKey(goodsType, on_delete=models.CASCADE)
