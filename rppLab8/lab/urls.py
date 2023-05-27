from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('createSeller/', views.createSeller, name="createSeller"),
    path('deleteSeller/<int:id>/', views.deleteSeller, name="deleteSeller"),
    path('updateSellerPage/<int:id>/', views.updateSellerPage, name="updateSellerPage"),
    path('updateSeller/<int:id>/', views.updateSeller, name="updateSeller"),

    path('createClient/', views.createClient, name='createClient'),
    path('deleteClient/<int:id>/', views.deleteClient, name="deleteClient"),
    path('updateClientPage/<int:id>/', views.updateClientPage, name="updateClientPage"),
    path('updateClient/<int:id>/', views.updateClient, name="updateClient"),

    path('createDish/', views.createDish, name='createDish'),
    path('deleteDish/<int:id>/', views.deleteDish, name="deleteDish"),
    path('updateDishPage/<int:id>/', views.updateDishPage, name="updateDishPage"),
    path('updateDish/<int:id>/', views.updateDish, name="updateDish"),

    path('createProduct/', views.createProduct, name='createProduct'),
    path('deleteProduct/<int:id>/', views.deleteProduct, name="deleteProduct"),
    path('updateProductPage/<int:id>/', views.updateProductPage, name="updateProductPage"),
    path('updateProduct/<int:id>/', views.updateProduct, name="updateProduct"),

    path('createOrder/', views.createOrder, name='createOrder'),
    path('deleteOrder/<int:id>/', views.deleteOrder, name="deleteOrder"),
    path('updateOrderPage/<int:id>/', views.updateOrderPage, name="updateOrderPage"),
    path('updateOrder/<int:id>/', views.updateOrder, name="updateOrder"),

    path('register', views.registerPage, name='registerPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logout')
]
