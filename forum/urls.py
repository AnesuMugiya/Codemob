from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
)
 
urlpatterns = [
    path('discussion-forum/', PostListView.as_view(), name='forum'),
    path('forum-posts/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # url with variable
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('detail/<int:id>/',views.detail,name='detail'),
]