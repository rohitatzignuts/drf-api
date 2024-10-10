from rest_framework.views import APIView
from rest_framework import generics, permissions
from blog.models import Blog
from blog.serializers import BlogSerializer
from blog.permissions import IsOwnerOrReadOnly


# Create your views here.
class BlogListCreate(generics.ListCreateAPIView):
    """
    List all blogs, or create a new blog.
    """

    permission_class = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogReadUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    Read, Update, Delete any single Blog
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "slug"
