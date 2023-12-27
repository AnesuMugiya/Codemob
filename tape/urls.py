from django.urls import path
from . import views

urlpatterns = [
     path('tape/', views.tape, name='tape'),
     path("channel/<slug>/", views.channel, name="studio"),
     path("upload/", views.upload_view, name="tape-upload"),
     path("uploading/", views.upload_processing, name="processing"),
     path("video_detail/", views.video_info_process, name="video-data"),
     path("watch/?v=<uuid:video_id>", views.video_watch_view, name="video_watch"),
     path("user_comment/<uuid:video_id>", views.video_comment, name="comment"),
     path("like/<uuid:id>/", views.liked_video, name="like-video"),
     path("channel/edit_video/<uuid:id>", views.update_video, name="update-video"),
     path("channel/delete_video/<uuid:id>", views.delete_video, name="delete-video"),
     path("dislike/<uuid:id>/", views.dislike_video, name="dislike-video"),
]