# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Permission

from api.authentication.models import User, Role

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)