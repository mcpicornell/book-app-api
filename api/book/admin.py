# -*- encoding: utf-8 -*-

from django.contrib import admin
from api.book.models import Book, Page

admin.site.register(Book)
admin.site.register(Page)
