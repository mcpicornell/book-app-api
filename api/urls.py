# -*- encoding: utf-8 -*-

from django.urls import include

from django.urls import path

urlpatterns = [
    path('authentication/', include('api.authentication.urls'), name='authentication'),
]
