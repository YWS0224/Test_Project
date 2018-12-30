from django.urls import path
from .views import *



app_name = 'l1'

urlpatterns = [
   path('GoodsType/', goodsTypes, name='goodsType'),
]


