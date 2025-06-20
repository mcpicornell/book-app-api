from rest_framework import serializers
from api.book.models import Book
from .page import PageSimpleSerializer


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ()
        read_only_fields = ('created_at', 'updated_at')


class BookDetailSerializer(serializers.ModelSerializer):
    pages = PageSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        exclude = ()
        read_only_fields = ('created_at', 'updated_at')