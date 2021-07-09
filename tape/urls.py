from django.urls import path
from . import views

urlpatterns = [
     path('tape/', views.tape, name='tape'),
     path("channel/<slug>/", views.channel, name="studio"),
     path("upload/", views.upload_view, name="tape-upload"),
     path("uploading/", views.upload_processing, name="processing"),
     path("video_detail/", views.video_info_process, name="video-data"),
]