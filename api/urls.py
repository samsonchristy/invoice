from django.contrib import admin
from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('invoices/', views.invoices), 
    path('invoices/<int:pk>/', views.invoices),
]
