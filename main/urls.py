
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name = 'index'),
    path("contact_form", views.contact_form, name = 'contact_form'),
    path('products', views.products, name = 'products')
]
