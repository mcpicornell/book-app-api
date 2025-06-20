import uuid

from django.db import models


class Page(models.Model): # A good name it could also be BookPage that would provide us information about the father Model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey('Book', related_name='pages', on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    content = models.TextField()

    class Meta:
        unique_together = ('book', 'number')
        ordering = ['number']

    def __str__(self):
        return f"Page {self.number} of {self.book.title}"
