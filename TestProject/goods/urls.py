from django.urls import path, re_path
from .views import *



app_name = 'l2'

urlpatterns = [
   re_path(r'^goods/(\d{1,2})', find_goods, name='findgoods'),
]

