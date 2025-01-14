from rest_framework import generics
from .models import Blog, Circular, Exam
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer, CircularSerializer, ExamSerializer, ExamDetailSerializer, ExamCreateSerializer
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


class ExamListView(APIView):
    def get(self, request):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)
    
class ExamDetailView(APIView):
    def get(self, request, exam_id):
        try:
            exam = Exam.objects.get(id=exam_id)
            serializer = ExamDetailSerializer(exam)
            return Response(serializer.data)
        except Exam.DoesNotExist:
            return Response({"error": "Exam not found"}, status=status.HTTP_404_NOT_FOUND)

class ExamCreateView(APIView):
    permission_classes = [IsStaffOrReadOnlyForAuthenticated]
    def post(self, request):
        serializer = ExamDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExamDeleteView(APIView):
    permission_classes = [IsStaffOrReadOnlyForAuthenticated]
    def delete(self, request, exam_id):
        try:
            exam = Exam.objects.get(id=exam_id)
            exam.delete()
            return Response({"message": "Exam deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exam.DoesNotExist:
            return Response({"error": "Exam not found"}, status=status.HTTP_404_NOT_FOUND)

