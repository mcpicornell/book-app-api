# -*- encoding: utf-8 -*-

from django.urls import include

from django.urls import path

urlpatterns = [
    path('auth/', include('api.authentication.urls'), name='authentication'),
    path('', include('api.book.urls'), name='book'),
]
