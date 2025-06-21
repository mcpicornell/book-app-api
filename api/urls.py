# -*- encoding: utf-8 -*-

from django.urls import include

from django.urls import path

urlpatterns = [
    # If we want an apps base route, it also can be auth/ or authentication/, it would
    path('', include('api.authentication.urls'), name='authentication'),

    path('', include('api.book.urls'), name='book'),
]
