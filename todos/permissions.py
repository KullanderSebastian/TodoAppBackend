from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	allows owners of tasks to edit them
	"""

	def has_object_permission(self, request, view, obj):
		#import pdb;pdb.set_trace()
		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.owner == request.user
