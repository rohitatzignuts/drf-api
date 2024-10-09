from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from task_management.models import Task
from task_management.serializers import TaskSerializer


# Create your views here.
class TaskListCreate(generics.ListCreateAPIView):
    """
    List all tasks, or create a new task.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    """
    Read, Update, Delete any single task
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
