from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.role == 'admin':
                return True
        return False


class IsAuthorOrStaffReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        staff = any((
            request.user.is_superuser,
            request.user.role == 'admin',
            request.user.role == 'moderator'
        ))
        if obj.author == request.user:
            return True
        if staff:
            return True
        return False
