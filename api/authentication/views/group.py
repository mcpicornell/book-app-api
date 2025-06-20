from django.contrib.auth.models import Group
from rest_framework import viewsets

from api.authentication.serializers import GroupSerializer
from api.permissions import RoleBasedAccessControlPermission


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [RoleBasedAccessControlPermission]
