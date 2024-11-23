# permissions.py
from rest_framework import permissions

class IsStaffUser(permissions.BasePermission):
    """
    Custom permission to only allow staff users to access the view.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a staff member
        return request.user and request.user.is_authenticated and request.user.is_staff


class IsStaffOrReadOnlyForAuthenticated(permissions.BasePermission):
    """
    Custom permission:
    - Staff users: Can CRUD (Create, Read, Update, Delete).
    - Authenticated non-staff users: Can only read (GET requests).
    - Unauthenticated users: No access.
    """

    def has_permission(self, request, view):
        # Allow full permissions for staff users
        if request.user and request.user.is_staff:
            return True

        # Allow read-only access for authenticated non-staff users
        if request.user and request.user.is_authenticated:
            return request.method in permissions.SAFE_METHODS  # GET, HEAD, OPTIONS

        # Deny access for unauthenticated users
        return False
