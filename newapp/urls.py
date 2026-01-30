from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('order/', views.form, name='form'),
    path('order/submit/', views.insertuser, name='ins'),
    path('success/', views.success, name='success'),
  
]
