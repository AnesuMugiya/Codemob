from django.shortcuts import render,redirect,get_object_or_404
from .forms import ChannelForm,EditChannelForm # VideoDataForm
from .models import Channel,VideoFiles,VideoDetail # ViewCount, VideoComment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
# Create your views here.

def tape(request):
     return render(request, 'tape/tape.html')


def create_channel(request):
    user=request.user
    if request.method =="POST":
        form=ChannelForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            category=form.cleaned_data.get('category')
            Channel.objects.create(name=name, user=user,slug=user.username, category=category)
            return redirect("mychannel", slug=user.username)

        return render(request, "tape/createchannel.html", context)

    else:
        form=ChannelForm()
        context={
            "channel_form":form
        }
    return render(request, "tape/createchannel.html", context)