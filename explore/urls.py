from django.urls import path
from . import views

urlpatterns = [
     path('explore/', views.explore, name='explore'),
]