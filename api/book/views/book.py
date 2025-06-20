from rest_framework import viewsets

from api.book.models import Book
from api.book.serializers import BookListSerializer, BookDetailSerializer
from api.permissions import RoleBasedAccessControlPermission


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [RoleBasedAccessControlPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return self.serializer_class
