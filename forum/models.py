from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
     title =  models.CharField(max_length=255)
     content = RichTextField(max_length=30000)
     created_at = models.DateTimeField(auto_now_add=True)
     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
     tags =  models.CharField(max_length=255, default='uncategorised')

     class Meta:
          ordering = ('-created_at',)

     def __str__(self):
          return self.title

     def get_absolute_url(self):
          return reverse("post-detail", kwargs={"pk": self.pk})

class Answer(models.Model):
     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='answers')
     content = RichTextField(max_length=30000)
     created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
          ordering = ('created_at',)

     def __str__(self):
          return self.content

class Comment(models.Model):
     answer = models.ForeignKey(Answer, blank=True, null=True, on_delete=models.CASCADE)
     post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
     comment = models.TextField(max_length=10000)
     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
          ordering = ('created_at',)
          
class UpVote(models.Model):
     answer = models.ForeignKey(Answer, blank=True, null=True, on_delete=models.CASCADE)
     post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvote_user')
     created_at = models.DateTimeField(auto_now_add=True)
     
class DownVote(models.Model):
     answer = models.ForeignKey(Answer, blank=True, null=True, on_delete=models.CASCADE)
     post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downvote_user')
     created_at = models.DateTimeField(auto_now_add=True)

class Flame(models.Model):
    post = models.ForeignKey(Post, blank=True, null=True, related_name='flames', on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, blank=True, null=True, related_name='flames', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='flames', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='flames', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)