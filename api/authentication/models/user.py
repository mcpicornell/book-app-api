import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # username, email and password are included in AbstractUser
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, related_name='users', blank=True, null=True)

    def __str__(self):
        return self.username
