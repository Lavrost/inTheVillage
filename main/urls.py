from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('realty', views.realty, name='realty'),
    path('realty_object', views.object_realty, name='object_realty'),
]