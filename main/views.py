from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from .models import RealtyObject


def home(request):
    return render(request, 'main/home.html')


def realty(request):
    realty_objects = RealtyObject.objects.all()
    return render(request, 'main/realty.html', {'realty_objects': realty_objects})


def object_realty(request):
    return render(request, 'main/object_realty.html')
