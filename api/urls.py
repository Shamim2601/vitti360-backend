from django.urls import path
from .views import BlogListCreateView, BlogDetailView, CircularListCreateView, CircularDetailView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog_list_create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('circulars/', CircularListCreateView.as_view(), name='circular-list-create'),
    path('circulars/<int:pk>/', CircularDetailView.as_view(), name='circular-detail'),
]
