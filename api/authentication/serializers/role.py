from rest_framework import serializers
from api.authentication.models import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        exclude = ()
