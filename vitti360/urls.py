from django.urls import path, include
from django.http import JsonResponse

urlpatterns = [
    path("", lambda request: JsonResponse({"message": "Server is running"})),
    path("auth/", include("authapp.urls")),
]