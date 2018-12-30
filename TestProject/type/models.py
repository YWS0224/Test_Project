from django.db import models


# Create your models here.
class goodsType(models.Model):
    typeName = models.DateField(max_length=20)
