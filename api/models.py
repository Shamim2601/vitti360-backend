from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('job', 'Job'),
        ('admission', 'Admission'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='job')  # Added category field
    author = models.CharField(max_length=100)  # Assuming author is a string, adjust if needed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Circular(models.Model):
    CATEGORY_CHOICES = [
        ('job', 'Job'),
        ('admission', 'Admission'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="circulars")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Exam(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField(default=60)
    category = models.CharField(max_length=100)
    num_questions = models.IntegerField(default=0)
    questions = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField(null=True, blank = True)
    end_at = models.DateTimeField(null=True, blank = True)

    def save(self, *args, **kwargs):
        # Automatically update the number of questions
        self.num_questions = len(self.questions or [])
        super().save(*args, **kwargs)