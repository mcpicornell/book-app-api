from rest_framework import serializers
from api.book.models import Page, Book

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'book', 'number', 'content']
