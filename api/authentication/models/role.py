import uuid

from django.contrib.auth.models import Group
from django.db import models


class Role(models.Model):
    NAME_EDITOR = 'editor'
    NAME_READER = 'reader'
    NAME_CHOICES = [
        (NAME_EDITOR, 'Editor'),
        (NAME_READER, 'Reader'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, choices=NAME_CHOICES, unique=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='roles')

    def __str__(self):
        return self.name


