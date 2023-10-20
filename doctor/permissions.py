from rest_framework import permissions


class IsDoctorOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the doctor object or has appropriate permissions
        # Modify this check as per your specific requirements
        print(request.user, obj)
        return (
            obj == request.user
        )  # This assumes the user is the owner, adjust as needed
