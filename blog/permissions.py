from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for all if the blog is not private
        if request.method in permissions.SAFE_METHODS:
            if obj.visibility == "PR" and obj.author != request.user:
                return False  # Deny access to non-owners for private blogs
            return True

        # Write permissions are only allowed to the author of the blog.
        return obj.author == request.user
