from django.contrib.auth.models import Group
from django.db import models


class Role(models.Model):
    EDITOR = 'editor'
    READER = 'reader'
    ROLE_CHOICES = [
        (EDITOR, 'Editor'),
        (READER, 'Reader'),
    ]
    name = models.CharField(max_length=20, choices=ROLE_CHOICES, unique=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='roles')


    def __str__(self):
        return self.name


