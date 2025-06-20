from rest_framework import serializers
from api.book.models import Page

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        exclude = ()

class PageSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        exclude = ('book',)