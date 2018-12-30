from django.db import models


# Create your models here.

class goods(models.Model):
    goodName = models.CharField(max_length=30)
    goodNum = models.IntegerField()
    goodPrice = models.FloatField()
