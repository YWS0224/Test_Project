from django.db import models


# Create your models here.

class goods(models.Model):
    goodName = models.CharField(max_length=30)
    goodNum = models.IntegerField()
    goodPrice = models.FloatField()
    goodType = models.ForeignKey('type.goodsType', to_field='id', on_delete=models.CASCADE)
