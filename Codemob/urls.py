"""Codemob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Default urls
from django.contrib import admin
from django.urls import path

# Custom urls, always remember to import every view you make here
from django.urls import path, include
from django.contrib.auth import views as auth_views

# Handles static files media and images
from django.conf import settings
from django.conf.urls.static import static

# Urls from Apps
from users import views as user_views
from forum import views as forum_views
from conversation.api import api_add_message

urlpatterns = [
    # Default
    path('admin/', admin.site.urls),

    # API 
    path('api/add_message/', api_add_message, name='api_add_message'),

    # Ajax comment
    path('save-answer-comment',forum_views.save_answer_comment,name='save-answer-comment'),
    path('save-question-comment',forum_views.save_question_comment,name='save-question-comment'),

    # Ajax upvote
    path('save-question-upvote',forum_views.save_question_upvote,name='save-question-upvote'),
    path('save-answer-upvote',forum_views.save_answer_upvote,name='save-answer-upvote'),

    # Ajax downvote
    path('save-question-downvote',forum_views.save_question_downvote,name='save-question-downvote'),
    path('save-answer-downvote',forum_views.save_answer_downvote,name='save-answer-downvote'),

    # Core App
    path('', include('core.urls')),

    # Forum App
    path('forum/', include('forum.urls')),

    # Conversation App
    path('conversation/', include('conversation.urls')),

    # Tape App
    path('tape/', include('tape.urls')),

    # Den App
    path('den/', include('den.urls')),

    # Explore App
    path('explore/', include('explore.urls')),

    # Users App
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('signup/', user_views.signup, name='signup'),
    path('preferences/', user_views.preferences, name='preferences'),  
    path('user/<str:username>/', user_views.profile, name='profile'),
    path('profile-update/', user_views.profile_update, name='profile_update'),
    path('user/<str:username>/follow/', user_views.follow_user, name='follow_user'),
    path('user/<str:username>/unfollow/', user_views.unfollow_user, name='unfollow_user'),
    path('user/<str:username>/followers/', user_views.followers, name='followers'),
    path('user/<str:username>/following/', user_views.following, name='following'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# This place is basically a table of contents of sorts.