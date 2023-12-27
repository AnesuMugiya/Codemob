import os
from django import template
import moviepy.editor
import datetime
from django.conf import settings
register = template.Library()

@register.filter(name='vduration')
def vduration(videourl):
    video = video = moviepy.editor.VideoFileClip(settings.PROJ_DIR + videourl)
    video_time = int(video.duration)
    video_time = str(datetime.timedelta(seconds=video_time))
    return video_time

