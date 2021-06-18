from django.urls import path
from . import views

urlpatterns = [
     path('den/', views.den, name='den'),
]