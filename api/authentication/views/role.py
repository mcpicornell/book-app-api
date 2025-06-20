from rest_framework import viewsets

from api.authentication.models import Role
from api.authentication.serializers import RoleSerializer
from api.permissions import RoleBasedAccessControlPermission


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [RoleBasedAccessControlPermission]
