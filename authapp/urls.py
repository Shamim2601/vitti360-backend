# urls.py
from django.urls import path
from .views import AllUsersView, CurrentUserView, DeleteUserView, RegisterUserView, UpdateCurrentUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', RegisterUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('delete/<str:username>/', DeleteUserView.as_view(), name='delete_user'),
    path('current_user/', CurrentUserView.as_view(), name='current_user'),
    path('current_user/update/', UpdateCurrentUserView.as_view(), name='update_current_user'),
    path('all_users/', AllUsersView.as_view(), name='all_users'),
]
