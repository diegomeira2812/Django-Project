from rest_framework import serializers
from .models import task_list

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task 
        fields = '__all__'