from django.contrib import admin
from django.urls import path
from firstApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.moviesInfo, name='movies'),
    path('sports/', views.sportsInfo, name='sports'),
    path('politics/', views.politicsInfo, name='politics'),
]
