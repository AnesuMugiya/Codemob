from django.shortcuts import render

# Create your views here.

def explore(request):
     return render(request, 'explore/explore.html')