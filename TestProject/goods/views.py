from django.shortcuts import render
from .models import *
from type.models import *

# Create your views here.


def find_goods(request, tid):
    fgoods = goods.objects.filter(goodType=tid)
    Types = goodsType.objects.all()
    return render(request, 'Index.html', {'fgoods': fgoods, 'Filtertype': Types})
