import uuid
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

def channel_directory_path(instance, filename):
    return "video_files/channel_{0}/{1}".format(instance.user.username, filename)


class VideoFiles(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video=models.FileField(upload_to=channel_directory_path)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    uploaded=models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('video_watch', args=[str(self.id)])

    def __str__(self):
        return f"video_file_{self.id}"

    def delete(self, *args, **kwargs):
        self.video.delete()
        super().delete(*args, **kwargs)

class VideoDetail(models.Model):
    videofile=models.OneToOneField(VideoFiles, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    thumbnail=models.ImageField(upload_to="thumbnail/")
    category=models.CharField(max_length=255, default='untagged')

    def __str__(self):
        return self.title


class ViewCount(models.Model):
    video=models.ForeignKey(VideoFiles, related_name="view_count", on_delete=models.CASCADE)
    ip_address=models.CharField(max_length=50)
    session=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.ip_address}"

class VideoComment(models.Model):
    video=models.ForeignKey(VideoFiles, related_name="comments", on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} comment"

class LikeTape(models.Model):
     video = models.ForeignKey(VideoFiles, blank=True, null=True, on_delete=models.CASCADE)
     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_vid')
     created_at = models.DateTimeField(auto_now_add=True)
     
class DislikeTape(models.Model):
     video = models.ForeignKey(VideoFiles, blank=True, null=True, on_delete=models.CASCADE)
     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dislike_vid')
     created_at = models.DateTimeField(auto_now_add=True)