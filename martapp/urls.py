
from django.contrib import admin
from django.urls import path
from martapp import views

urlpatterns = [
    
    path('about/', views.about, name= 'about'),

    path('contact/', views.contact, name = 'contact'),

    path('', views.index, name= 'index'),

    path('services/', views.services, name= 'services'),

    path('prices/', views.prices, name= 'prices'),
    
    

]
