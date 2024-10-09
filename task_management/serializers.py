from rest_framework import serializers
from task_management.models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "description", "created", "tag", "status", "owner_id"]
