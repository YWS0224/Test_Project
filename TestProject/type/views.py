from django.shortcuts import render
from .models import *


# Create your views here.


def goodsTypes(request):
    Types = goodsType.objects.all()
    return render(request, 'Index.html', {'Filtertype': Types})
