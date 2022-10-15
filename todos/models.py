from django.db import models

# Create your models here.

class Task(models.Model):
	owner = models.ForeignKey("auth.User", related_name="todos", on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200)
	completed = models.BooleanField(default=False, blank=True, null=True)
	objects = models.Manager()

	def __str___(self):
		return self.title

	class Meta:
		ordering = ["created"]
