from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('weather_delete/<int:weather_id>/',  views.weather_delete,  name='weather_delete'),
]