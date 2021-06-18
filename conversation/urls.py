from django.urls import path
from . import views

urlpatterns = [
         path('messaging/', views.conversations, name='conversations'),
         path('messaging/<int:user_id>/', views.conversation, name='conversation'),
         path('messanger/', views.messaging, name='messaging'),
]