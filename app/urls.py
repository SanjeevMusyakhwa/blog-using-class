
from django.urls import path
from app import views
urlpatterns = [
    path('', views.PostListView.as_view(), name='postList'),
    path('postDetail/<int:pk>/', views.PostDetailView.as_view(), name='postDetail'),
    path('draftList/', views.DraftListView.as_view(), name='draftList'),
    path('draftDetail/<int:pk>/', views.DraftDetailView.as_view(), name='draftDetail'),
]
