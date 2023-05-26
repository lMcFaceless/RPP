from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('createSeller/', views.createSeller, name = "createSeller"),
    path('deleteSeller/<int:id>/', views.deleteSeller, name = "deleteSeller"),
    path('updateSellerPage/<int:id>/', views.updateSellerPage, name = "updateSellerPage"),
    path('updateSeller/<int:id>/', views.updateSeller, name = "updateSeller")
]