from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwner, IsAdminOrSelf
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["username", "email"]
    ordering_fields = ["username", "email"]

    def get_permissions(self):
        if self.action in ["create", "register"]:
            return [AllowAny()]
        return [IsAdminOrSelf()]

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
            "message": "User registered successfully",
            "user": serializer.data
        }, status=status.HTTP_201_CREATED )

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def profile(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status", "due_date", "priority"]
    search_fields = ["title", "description"]
    ordering_fields = ["due_date", "priority", "created_at"]

    def get_queryset(self):
        # Return tasks only for the logged-in user
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Set the owner of the task to the logged-in user
        serializer.save(owner=self.request.user)
    
    # @action(detail= True, methods=["patch"],permission_classes=[IsAuthenticated, IsOwner] )
    # def complete(self, request, pk=None):
    #     task = self.get_object()
    #     task.mark_completed()
    #     serializer = self.get_serializer(task)
    #     return Response( serializer.data, status=status.HTTP_200_OK)

    # @action(detail=True, methods=["patch"],permission_classes=[IsAuthenticated, IsOwner] )
    # def incomplete(self, request, pk=None):
    #     task =self.get_object()
    #     task.mark_incomplete()
    #     serializer = self.get_serializer(task)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated, IsOwner])
    def complete(self, request, pk=None):
        task = self.get_object()
        if task.status == 'completed':
            task.mark_incomplete()
        else:
            task.mark_completed()
        serializer = self.get_serializer(task)
        return Response(serializer.data)
