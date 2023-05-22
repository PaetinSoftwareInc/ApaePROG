
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('mission/', views.mission, name='mission'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
]


