from django.shortcuts import render, redirect
from django.urls import reverse_lazy 
from django.views.generic import ListView,DetailView, CreateView, UpdateView, View
from app.models import Post
from app.forms import PostForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
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
  
class DraftListView(LoginRequiredMixin,ListView):
  model = Post
  template_name = 'draftList.html'
  context_object_name = 'posts'

  def get_queryset(self):
    posts = Post.objects.filter(published_at__isnull = True).order_by('-published_at')
    return posts

class DraftDetailView(LoginRequiredMixin,DetailView):
  model = Post
  template_name='draftDetail.html'
  context_object_name = 'post'

  def get_queryset(self):
    post = Post.objects.filter(pk = self.kwargs['pk'], published_at__isnull = True)
    return post
  
class CreatePostView(LoginRequiredMixin, CreateView):
  model = Post
  template_name = 'postCreate.html'
  form_class = PostForm
  # success_url = reverse_lazy("postList")

  def get_success_url(self) -> str:
    return reverse_lazy('draftDetail', kwargs= {'pk': self.object.pk})

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
class UpdatePostView(LoginRequiredMixin, UpdateView):
  model = Post
  template_name = 'postCreate.html'
  form_class = PostForm

  def get_success_url(self):
    post = self.get_object()
    if post.published_at:
      return reverse_lazy('postDetail', kwargs = {'pk': post.pk})
    else:
      return reverse_lazy('draftDetail', kwargs = {'pk': post.pk})
    
class PublishPostView(LoginRequiredMixin, View):
  def get(self, request, pk):
    post = Post.objects.get(pk = pk , published_at__isnull= True)
    post.published_at = timezone.now()
    post.save()
    return redirect('postDetail', pk)
  
class DeletePostView(LoginRequiredMixin, View):
  def get(self, request, pk):
    post = Post.objects.get(pk = pk)
    post.delete()
    return redirect('postList')
  
  def form(self, form):
    messages.success(self.request, "Post Deleted Successfully")
    return super().form_valid(form)
