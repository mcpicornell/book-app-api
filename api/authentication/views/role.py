from rest_framework import viewsets
from api.authentication.models import Role
from api.authentication.serializers import RoleSerializer
from rest_framework.permissions import IsAuthenticated

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]