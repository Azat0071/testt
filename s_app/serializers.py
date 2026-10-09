from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200, allow_blank=True)
    description = serializers.CharField(allow_blank=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    completed = serializers.BooleanField(default=False)

    class Meta:
        model = Task
        fields = '__all__'