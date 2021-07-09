from django.shortcuts import render,redirect,get_object_or_404
# from .forms import VideoDataForm
from .models import VideoFiles,VideoDetail # ViewCount, VideoComment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.

def tape(request):
     return render(request, 'tape/tape.html')

def channel(request, slug):

    return render(request, "tape/studio.html")

@login_required
def upload_view(request):
    return render(request, "tape/tapeupload.html")

def upload_processing(request):
    if request.method =="POST":
        file=request.FILES['file']
        username = request.user.username
        user = get_object_or_404(User, username=username)
        upload=VideoFiles.objects.create(video=file, user=user)
        data={
            'video_id':upload.id,
            "video_path":upload.video.url
        }
        return JsonResponse(data, safe=False)
    return JsonResponse({'error':'an error ocurred'})
    