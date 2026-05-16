from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contact/merci/', views.contact_merci, name='contact_merci'),
    path('cookies/', views.cookies, name='cookies'),
]
