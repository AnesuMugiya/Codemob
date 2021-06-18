from django.shortcuts import render

# Create your views here.

def tape(request):
     return render(request, 'tape/tape.html')