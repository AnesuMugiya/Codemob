from django.urls import path
from . import views

urlpatterns = [
     path('tape/', views.tape, name='tape'),
     path('createchannel/', views.create_channel, name='createchannel'),
]