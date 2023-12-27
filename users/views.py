from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login 
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from forum.models import Post
# Create your views here.

def signup(request):
     if request.method == 'POST':
          form = UserRegisterForm(request.POST)
          if form.is_valid():
               form.save()
               user = form.save()
               login(request, user)
               username = form.cleaned_data.get('username')
               messages.success(request, f'Account created for {username}!')
               return redirect('preferences')

     else:
          form = UserRegisterForm()
     return render(request, 'users/signup.html', {'form': form})

@login_required
def preferences(request):
     return render(request, 'users/preferences.html')


@login_required
def profile_update(request): 
     if request.method == 'POST':
          u_form = UserUpdateForm(request.POST, instance=request.user)
          p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

          if u_form.is_valid() and p_form.is_valid():
               u_form.save()
               p_form.save()
          # Redirects you back to the profile page, preventing that resubmission thingy
          messages.success(request, f'Your account has been updated!')
          return redirect('profile_update')
     
     else:
          u_form = UserUpdateForm(instance=request.user)
          p_form = ProfileUpdateForm(instance=request.user.profile)

     context = {
          'u_form': u_form,
          'p_form': p_form
     }
     return render(request, 'users/profile_update.html', context)

def profile(request, username): 
     user = get_object_or_404(User, username=username)
     post = Post.objects.filter(created_by=user.id)

     context = {
          'user': user,
          'post': post
     }

     return render(request, 'users/profile.html', context)

@login_required
def follow_user(request, username):
     user = get_object_or_404(User, username=username)

     request.user.profile.follows.add(user.profile)

     return redirect('profile', username=username)
 
@login_required
def unfollow_user(request, username):
     user = get_object_or_404(User, username=username)

     request.user.profile.follows.remove(user.profile)

     return redirect('profile', username=username)

def followers(request, username):
     user = get_object_or_404(User, username=username)

     return render(request, 'users/followers.html', {'user': user})


def following(request, username):
     user = get_object_or_404(User, username=username)

     return render(request, 'users/following.html', {'user': user})

