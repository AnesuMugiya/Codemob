from django.shortcuts import render

# Create your views here.

def den(request):
     return render(request, 'den/den.html')
