from rest_framework import generics
from .models import Blog, Circular
from .serializers import BlogSerializer, CircularSerializer
from authapp.permissions import IsStaffOrReadOnlyForAuthenticated

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsStaffOrReadOnlyForAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsStaffOrReadOnlyForAuthenticated]

class CircularListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all circulars and creating a new circular.
    """
    queryset = Circular.objects.all()
    serializer_class = CircularSerializer
    permission_classes = [IsStaffOrReadOnlyForAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the current user as the author
        serializer.save(author=self.request.user)

class CircularDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a specific circular.
    """
    queryset = Circular.objects.all()
    serializer_class = CircularSerializer
    permission_classes = [IsStaffOrReadOnlyForAuthenticated]