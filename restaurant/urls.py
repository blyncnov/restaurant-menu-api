"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.urls import path
from restaurant import views

urlpatterns = [
    path("", views.get_restaurants, name="all-restaurants" ),
    path("<int:restaurant_id>", views.get_restaurant, name="get-restaurants" )
]
