from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

# Create your views here.

class PostList(generics.ListCreateAPIView):
    """
    List all posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List a single posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer