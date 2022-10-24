from todos.models import Task
from todos.serializers import TaskSerializer, UserSerializer
from rest_framework import generics, permissions, viewsets
from django.contrib.auth.models import User
from todos.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	permission_classes = [IsOwnerOrReadOnly]

	@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	def get_queryset(self):
		user = self.request.user
		if self.request.user.is_anonymous:
			return Task.objects.all()

		return Task.objects.filter(owner=user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView): 
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.AllowAny]

@api_view(["GET"])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'tasks': reverse('task-list', request=request, format=format)
	})
