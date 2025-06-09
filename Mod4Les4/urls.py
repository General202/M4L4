from django.contrib import admin
from django.urls import path
from Mod4Les4 import views

urlpatterns = [
    path('', views.main_page),

] 