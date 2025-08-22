from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer
from notifications.models import Notification

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            # create notification
            Notification.objects.create(
                recipient=post.user,
                actor=request.user,
                verb="liked your post",
                target=post
            )
            return Response({"status": "post liked"})
        return Response({"status": "already liked"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"status": "post unliked"})
        except Like.DoesNotExist:
            return Response({"status": "not liked"}, status=status.HTTP_400_BAD_REQUEST)
