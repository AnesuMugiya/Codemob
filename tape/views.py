from django.shortcuts import render,redirect,get_object_or_404
from .forms import VideoDataForm
from .models import VideoFiles,VideoDetail, ViewCount, VideoComment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.

def tape(request):
    tapes=VideoFiles.objects.all()
    context={
        "videos": tapes,
    }
    return render(request, "tape/tape.html", context)

@login_required
def channel(request, slug):
    username = request.user.username
    user = get_object_or_404(User, username=username)
    myvideos=VideoFiles.objects.filter(user=user)
    context={
        "channel":user,
        "videos":myvideos

    }
    
    return render(request, "tape/studio.html", context)

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

def video_info_process(request):
    if request.method == "POST":
        file_id=request.POST['videofile']
        title=request.POST['title']
        desc=request.POST['description']
        category=request.POST['category']
        thumbnail=request.FILES['thumbnail']

        video=get_object_or_404(VideoFiles, id=file_id)
        VideoDetail.objects.create(videofile=video,title=title, description=desc, thumbnail=thumbnail, category=category,)
         #message video uploaded successful
        return redirect('studio', slug=request.user.username)
    return redirect('file-upload')

def video_watch_view(request, video_id):
    video=get_object_or_404(VideoFiles, id=video_id)

    ip=request.META['REMOTE_ADDR']
    if not ViewCount.objects.filter(video=video, session=request.session.session_key):
        view=ViewCount(video=video, ip_address=ip, session=request.session.session_key)
        view.save()
    video_views=ViewCount.objects.filter(video=video).count()

    context={
        "tape":video,
        "view_count":video_views
    }

    return render(request, "tape/watch.html", context)


@login_required
def liked_video(request, id):
    user=request.user
    Like=False
    if request.method=="POST":
        video_id=request.POST['video_id']
        get_video=get_object_or_404(VideoFiles, id=video_id)
        if user in get_video.likes.all():
            get_video.likes.remove(user)
            Like=False
        else:
            get_video.likes.add(user)
            Like=True
        data={
            "liked":Like,
            "likes_count":get_video.likes.all().count()
        }
        return JsonResponse(data, safe=False)
    return redirect(reverse('video_watch', args=[str(id)]))


@login_required
def dislike_video(request, id):
    user=request.user
    Dislikes=False
    if request.method == "POST":
        video_id=request.POST['video_id']
        print("printing ajax id", video_id)
        watch=get_object_or_404(VideoFiles, id=video_id)
        if user in watch.dislikes.all():
            watch.dislikes.remove(user)
            Dislikes=False
        else:
            if user in watch.likes.all():
                watch.likes.remove(user)
            watch.dislikes.add(user)
            watch.save()
            Dislikes=True
        data={
            "disliked":Dislikes,
            'dislike_count':watch.dislikes.all().count()
        }
        return JsonResponse(data, safe=False)
    return redirect(reverse('video_watch', args=[str(id)]))
            

@login_required
def video_comment(request, video_id):
    if request.method =="POST":
        comment=request.POST['comment']
        video=VideoFiles.objects.get(id=video_id)
        if comment is not None:
            create_comment=VideoComment(video=video, user=request.user, comment=comment)
            create_comment.save()
    return redirect('video_watch', video_id=video_id)


def update_video(request, id):
    video=VideoFiles.objects.get(id=id)
    form=VideoDataForm(instance=video.videodetail)
    if request.method=="POST":
        form=VideoDataForm(request.POST, request.FILES, instance=video.videodetail)
        if form.is_valid():
            form.save()
            return redirect("studio", slug=video.user.username)
    context={
        "update_form":form
    }
    return render(request, "tape/video-update.html", context)

def delete_video(request, id):
    video=VideoFiles.objects.get(id=id)
    if request.method=="POST":
        video.delete()
        return redirect("studio", slug=request.user.username)
    context={
        "video":video
    }
    return render(request, "tape/delete_video.html", context)