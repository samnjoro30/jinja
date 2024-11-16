from django.contrib import admin
from django.urls import path
from . import views


urlpatterns= [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio_details, name="page"),
    path('services/', views.service_details, name="services"),
    path('start/', views.starter, name="starter"),
]