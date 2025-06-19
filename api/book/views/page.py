from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.book.models import Page
from api.book.serializers import PageSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated]