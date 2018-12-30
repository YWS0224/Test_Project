from django.db import models


# Create your models here.
class goodsType(models.Model):
    typeName = models.CharField(max_length=20)
