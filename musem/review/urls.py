from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('review/', views.review),
    path('message/', views.message),
]
