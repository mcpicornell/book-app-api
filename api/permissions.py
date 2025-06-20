from django.contrib.auth.models import Permission
from rest_framework import exceptions
from rest_framework.permissions import DjangoModelPermissions

class RoleBasedAccessControlPermission(DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def get_required_permissions(self, method, model_cls):
        """
        Given a model and an HTTP method, return the list of permission
        codes that the user is required to have.
        """
        kwargs = {
            'app_label': model_cls._meta.app_label,
            'model_name': model_cls._meta.model_name
        }

        if method not in self.perms_map:
            raise exceptions.MethodNotAllowed(method)

        return [perm % kwargs for perm in self.perms_map[method]]

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        if not user.role:
            return False

        try:
            model_cls = view.queryset.model
        except AttributeError:
            return False

        required_perms = self.get_required_permissions(request.method, model_cls)

        role_permissions = Permission.objects.filter(group__in=user.role.groups.all())
        user_permissions = {f"{permission.content_type.app_label}.{permission.codename}" for permission in
                            role_permissions}

        return all(permission in user_permissions for permission in required_perms)
