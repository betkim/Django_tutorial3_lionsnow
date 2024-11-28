from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings

app_name = "page" 

urlpatterns = [
    path('', views.index, name='index'),


]
