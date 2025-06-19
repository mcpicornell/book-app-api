from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.book.models import Book
from api.book.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
