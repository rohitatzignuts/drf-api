from rest_framework import serializers
from task_management.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "description", "created", "tag", "status"]
