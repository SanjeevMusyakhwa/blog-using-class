
from django.urls import path
from app import views
urlpatterns = [
    path('', views.PostListView.as_view(), name='postList')
]
