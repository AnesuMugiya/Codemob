from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
     ListView, 
     DetailView, 
     CreateView, 
     UpdateView, 
     DeleteView
)
from .models import Post, Answer, Comment, UpVote, DownVote
from django import forms
from .forms import AnswerForm
from datetime import datetime


def forum(request):
     posts = Post.objects.all()
     tags = Post.tags
     context = {
          'posts': posts,
          
          'tags': Post.tags
     }

     return render(request, 'forum/discussion-forum.html', context)
     

class PostListView(ListView):
     model = Post
     # Setting an existing template
     template_name = 'forum/discussion-forum.html' # <app>/<model>_<viewtype>.html
     context_object_name = 'posts'
     # Ordering posts from latest to oldest
     ordering = ['-created_at']
     # Allows pagination of posts
     paginate_by = 7

# Showing posts for specific user
class UserPostListView(ListView):
     model = Post
     # Setting an existing template
     template_name = 'forum/user_posts.html' 
     # <app>/<model>_<viewtype>.html
     context_object_name = 'posts'
     # Allows pagination of posts
     paginate_by = 5
     
     def get_queryset(self):
          user = get_object_or_404(User, username=self.kwargs.get('username'))
          return Post.objects.filter(created_by=user).order_by('-created_at')

class PostDetailView(DetailView):
     model = Post
     template_name = 'forum/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
     model = Post
     fields = ['title', 'content', 'tags']

     # Telling django that the currently logged in user is the author
     def form_valid(self, form):
          form.instance.created_by = self.request.user
          return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
     model = Post
     fields = ['title', 'content', 'tags']

     # Telling django that the currently logged in user is the author
     def form_valid(self, form):
          form.instance.created_by = self.request.user
          return super().form_valid(form)

     #makes sure that users can only update their own posts
     def test_func(self):
          post = self.get_object()
          if self.request.user == post.created_by:
               return True
          return False

# Allows users to delete post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
     model = Post
     success_url = '/forum/discussion-forum/'
     #makes sure that users can only update their own posts
     def test_func(self):
          post = self.get_object()
          if self.request.user == post.created_by:
               return True
          return False

def detail(request,id):
    question = Post.objects.get(pk=id)
    tags = question.tags.split(',')
    answers = Answer.objects.filter(post=question)
    answerform=AnswerForm
    if request.method=='POST':
        answerData=AnswerForm(request.POST)
        if answerData.is_valid():
            answer=answerData.save(commit=False)
            answer.post=question
            answer.created_by=request.user
            answer.save()
            messages.success(request,'Answer has been submitted.')
   
    return render(request,'forum/detail.html',{
        'question': question,
        'tags': tags,
        'answers': answers,
        'answerform':answerform
    })

# Save answer comment
def save_answer_comment(request):
     if request.method=='POST':
          comment = request.POST['comment']
          answerid = request.POST['answerid']
          answer = Answer.objects.get(pk=answerid)
          created_by = request.user
          Comment.objects.create(
               answer=answer,
               comment=comment,
               created_by=created_by
          )
          return JsonResponse({'bool':True})

# Save question comment
def save_question_comment(request):
     if request.method=='POST':
          comment = request.POST['comment']
          questionid = request.POST['questionid']
          post = Post.objects.get(pk=questionid)
          created_by = request.user
          Comment.objects.create(
               post=post,
               comment=comment,
               created_by=created_by
          )
          return JsonResponse({'bool':True})

# Save answer upvote
def save_answer_upvote(request):
     if request.method=='POST':
          answerid = request.POST['answerid']
          answer = Answer.objects.get(pk=answerid)
          created_by = request.user
          check = UpVote.objects.filter(answer=answer,created_by=created_by).count()
          if check > 0:
               return JsonResponse({'bool':False})
          UpVote.objects.create(
               answer=answer,
               created_by=created_by
          )
          return JsonResponse({'bool':True})

# Save question upvote
def save_question_upvote(request):
     if request.method=='POST':
          questionid = request.POST['questionid']
          post = Post.objects.get(pk=questionid)
          created_by = request.user
          check = UpVote.objects.filter(post=post,created_by=created_by).count()
          if check > 0:
               return JsonResponse({'bool':False})
          UpVote.objects.create(
               post=post,
               created_by=created_by
          )
          return JsonResponse({'bool':True})



# Save answer downvote
def save_answer_downvote(request):
     if request.method=='POST':
          answerid = request.POST['answerid']
          answer = Answer.objects.get(pk=answerid)
          created_by = request.user
          check = DownVote.objects.filter(answer=answer,created_by=created_by).count()
          if check > 0:
               return JsonResponse({'bool':False})
          DownVote.objects.create(
               answer=answer,
               created_by=created_by
          )
          return JsonResponse({'bool':True})

# Save question upvote
def save_question_downvote(request):
     if request.method=='POST':
          questionid = request.POST['questionid']
          post = Post.objects.get(pk=questionid)
          created_by = request.user
          check = DownVote.objects.filter(post=post,created_by=created_by).count()
          if check > 0:
               return JsonResponse({'bool':False})
          DownVote.objects.create(
               post=post,
               created_by=created_by
          )
          return JsonResponse({'bool':True})

     