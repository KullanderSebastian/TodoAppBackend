from rest_framework import serializers
from todos.models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source="owner.username")

	class Meta:
		model = Task
		fields = ["url", "owner", "id", "title", "completed"]

	def create(self, validated_data):
		"""
		Create and return a "Task"
		"""
		return Task.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return a "Task"
		"""
		instance.completed = validated_data.get("title", instance.title)
		instance.completed = validated_data.get("completed", instance.completed)
		instance.save()
		return instance

class UserSerializer(serializers.HyperlinkedModelSerializer):
	todos = serializers.HyperlinkedRelatedField(many=True, view_name="task-detail", read_only=True)

	class Meta:
		model = User
		fields = ["url", "id", "username", "todos"]
