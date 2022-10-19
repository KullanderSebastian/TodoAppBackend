from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todos import views

router = DefaultRouter()
router.register(r"tasks", views.TaskViewSet, basename="task")
router.register(r"users", views.UserViewSet, basename="user")

urlpatterns = [
	path("", include(router.urls)),
	path("account/register/", views.UserCreate.as_view()),
]
