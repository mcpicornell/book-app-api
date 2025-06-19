# -*- encoding: utf-8 -*-

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.book.views import BookViewSet, PageViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'pages', PageViewSet, basename='pages')

urlpatterns = [
    path('', include(router.urls)),
]