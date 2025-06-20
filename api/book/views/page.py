from rest_framework import viewsets

from api.book.models import Page
from api.book.serializers import PageSerializer
from api.permissions import RoleBasedAccessControlPermission


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [RoleBasedAccessControlPermission]
