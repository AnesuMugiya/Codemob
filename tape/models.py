import uuid
from django.db import models
from django.contrib.auth.models import User

def channel_directory_path(instance, filename):
    return "video_files/channel_{0}/{1}".format(instance.user.username, filename)


class VideoFiles(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    video=models.FileField(upload_to=channel_directory_path)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    uploaded=models.DateTimeField(auto_now_add=True)
   #  likes=models.ManyToManyField(User, related_name="video_loved")
   #  dislikes=models.ManyToManyField(User, related_name="video_disliked")

   #  def __str__(self):
   #      return f"video_file_{self.id}"

   #  def delete(self, *args, **kwargs):
   #      self.video.delete()
   #      super().delete(*args, **kwargs)

   #  def get_absolute_url(self):
   #      return reverse('video_watch', args=[str(self.id)])
    
   #  def num_likes(self):
   #      return self.likes.count()

   #  def num_dislikes(self):
   #      return self.dislikes.count()

class VideoDetail(models.Model):
    videofile=models.OneToOneField(VideoFiles, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    thumbnail=models.ImageField(upload_to="thumbnail/")
    category=models.CharField(max_length=255, default='untagged')

    def __str__(self):
        return self.title