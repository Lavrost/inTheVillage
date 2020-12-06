from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def home(request):
    return render(request, 'main/home.html')


def realty(request):
    realty_objects = RealtyObject.objects.all()
    return render(request, 'main/realty.html', {'realty_objects': realty_objects})


def object_realty(request):
    """ Отрисовка шаблона одного объекта недвижимости"""
    pass