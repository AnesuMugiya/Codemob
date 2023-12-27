from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.models import Profile
from forum.models import Post

# Create your views here.
def index(request):
     # Here we're rendering the Html for the landing page for none logged in users
     return render(request, 'core/index.html')

# Landing page for logged in users
@login_required
def home(request):

     return render(request, 'core/home.html')



# About Page
def about(request):
     return render(request, 'core/about.html')

# Search function
def search(request):
     query = request.GET.get('query', '')

     if len(query) > 0:
          users = User.objects.filter(username__icontains=query)
          posts = Post.objects.filter(content__icontains=query)
     else:
          users = []
          posts = []

     context = {
          'query': query,
          'users': users,
          'posts': posts
     }
     return render(request, 'core/search.html', context)