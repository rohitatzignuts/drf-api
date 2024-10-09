from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions
from task_management.models import Task
from task_management.serializers import TaskSerializer
from task_management.permissions import IsOwnerOrReadOnly


# Create your views here.
class TaskListCreate(generics.ListCreateAPIView):
    """
    List all tasks, or create a new task.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    Read, Update, Delete any single task
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
