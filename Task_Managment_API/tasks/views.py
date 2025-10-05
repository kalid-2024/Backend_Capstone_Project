from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
# from .permissions import IsOwner, IsAdminOrSelf
from rest_framework.permissions import IsAuthenticated, AllowAny

User = get_user_model()
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["due_date", "priority", "created_at"]

    def perform_create(self, serializer):
        # Set the owner of the task to the logged-in user
        serializer.save(owner=self.request.user)
    