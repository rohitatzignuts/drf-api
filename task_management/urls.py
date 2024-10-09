from django.contrib import admin
from django.urls import path, include
from task_management.views import TaskListCreate, TaskRetrieveUpdateDelete

urlpatterns = [
    path("", TaskListCreate.as_view(), name="task-list-create"),
    path(
        "<int:pk>/",
        TaskRetrieveUpdateDelete.as_view(),
        name="task-detail",
    ),
]
