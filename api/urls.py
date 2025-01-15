from django.urls import path
from .views import BlogListCreateView, BlogDetailView, CircularListCreateView, CircularDetailView,ExamListView, ExamCreateView, ExamDetailView, ExamDeleteView, PerformanceCreateView, PerformanceListView, PerformanceDeleteView    

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog_list_create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('circulars/', CircularListCreateView.as_view(), name='circular-list-create'),
    path('circulars/<int:pk>/', CircularDetailView.as_view(), name='circular-detail'),
    path('exams/', ExamListView.as_view(), name='exam-list'),  # For listing exams
    path('exams/create/', ExamCreateView.as_view(), name='exam-create'),  # For creating exams
    path('exams/<int:exam_id>/', ExamDetailView.as_view(), name='exam-detail'),  # For exam details
    path('exams/<int:exam_id>/delete/', ExamDeleteView.as_view(), name='exam-delete'),  # For deleting exams
    path('performances/', PerformanceListView.as_view(), name='performance-list'),
    path('performances/create/', PerformanceCreateView.as_view(), name='performance-create'),
    path('performances/<int:pk>/delete/', PerformanceDeleteView.as_view(), name='performance-delete'),
]
