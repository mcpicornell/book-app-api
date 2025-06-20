# -*- encoding: utf-8 -*-

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from api.authentication.views import UserViewSet, RoleViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'roles', RoleViewSet, basename='roles')
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),

]