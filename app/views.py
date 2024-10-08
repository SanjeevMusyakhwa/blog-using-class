from django.shortcuts import render
from django.views.generic import ListView
from app.models import Post
# Create your views here.

class PostListView(ListView):
  model = Post
  template_name = 'postList.html'
  context_object_name = "posts"
