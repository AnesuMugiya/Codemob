from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('index/', views.index, name='index'),
     path('about/', views.about, name='about'),
     path('search/', views.search, name='search'), 
]