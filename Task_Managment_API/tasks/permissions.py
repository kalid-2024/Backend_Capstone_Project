from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsAdminOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff
