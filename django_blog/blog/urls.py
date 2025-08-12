from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-new'),  # create
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # read
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # update
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # delete
]
