from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return object.owner = request.user

class IsAdminorSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff
