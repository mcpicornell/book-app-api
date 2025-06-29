from django.contrib.auth import get_user_model
from rest_framework import viewsets

from api.authentication.serializers import UserSerializer
from api.permissions import RoleBasedAccessControlPermission


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [RoleBasedAccessControlPermission]
