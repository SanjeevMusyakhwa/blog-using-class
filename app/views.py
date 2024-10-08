from django.shortcuts import render
from django.views.generic import ListView,DetailView
from app.models import Post
# Create your views here.

class PostListView(ListView):
  model = Post
  template_name = 'postList.html'
  context_object_name = "posts"

  # for Filtering 
  def get_queryset(self):
    posts = Post.objects.filter(published_at__isnull= False).order_by('-published_at')
    return posts

class PostDetailView(DetailView):
  model = Post
  template_name = 'postDetail.html'
  context_object_name = 'post'

  def get_queryset(self):
    post = Post.objects.filter(pk = self.kwargs['pk'], published_at__isnull = False)
    return post
