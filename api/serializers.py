from rest_framework import serializers
from .models import Blog, Circular, Exam, Performance

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'category', 'author', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

class CircularSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Circular
        fields = ['id', 'title', 'description', 'category', 'author', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'title', 'duration', 'category', 'num_questions', 'created_at', 'start_at', 'end_at']

class ExamDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'title', 'duration', 'category', 'num_questions', 'created_at', 'start_at', 'end_at', 'questions']

class ExamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title', 'duration', 'category', 'questions', 'start_at', 'end_at']

class PerformanceSerializer(serializers.ModelSerializer):
    exam_details = serializers.SerializerMethodField()

    class Meta:
        model = Performance
        fields = ['id', 'username', 'correct_count', 'exam_duration', 'examId', 'exam_details']

    def get_exam_details(self, obj):
        return {
            "title": obj.examId.title,
            "category": obj.examId.category,
            "duration": obj.examId.duration,
            "num_questions": obj.examId.num_questions,
            "created_at": obj.examId.created_at
        }