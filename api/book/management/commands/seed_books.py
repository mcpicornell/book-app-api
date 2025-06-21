import random

from django.core.management.base import BaseCommand

from api.book.models import Book, Page


class SeedBooksManager:
    BOOKS_SAMPLE = [
        {"title": "1984", "author": "George Orwell"},
        {"title": "Brave New World", "author": "Aldous Huxley"},
        {"title": "Fahrenheit 451", "author": "Ray Bradbury"},
        {"title": "Animal Farm", "author": "George Orwell"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "Lord of the Flies", "author": "William Golding"},
        {"title": "The Catcher in the Rye", "author": "J.D. Salinger"},
        {"title": "Moby-Dick", "author": "Herman Melville"},
        {"title": "Pride and Prejudice", "author": "Jane Austen"},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
        {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky"},
        {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky"},
        {"title": "Jane Eyre", "author": "Charlotte Brontë"},
        {"title": "Wuthering Heights", "author": "Emily Brontë"},
        {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde"},
        {"title": "Frankenstein", "author": "Mary Shelley"},
        {"title": "Dracula", "author": "Bram Stoker"},
        {"title": "The Stranger", "author": "Albert Camus"},
        {"title": "Catch-22", "author": "Joseph Heller"}
    ]

    BOOKS_CONTENT = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",
        "Duis aute irure dolor in reprehenderit in voluptate velit esse.",
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa.",
        "Cras mattis consectetur purus sit amet fermentum.",
        "Integer posuere erat a ante venenatis dapibus.",
        "Nullam id dolor id nibh ultricies vehicula ut id elit.",
        "Curabitur blandit tempus porttitor.",
        "Maecenas sed diam eget risus varius blandit sit amet.",
        "Vivamus sagittis lacus vel augue laoreet rutrum faucibus.",
        "Aenean lacinia bibendum nulla sed consectetur.",
        "Morbi leo risus, porta ac consectetur ac, vestibulum at eros.",
        "Praesent commodo cursus magna, vel scelerisque nisl consectetur.",
        "Etiam porta sem malesuada magna mollis euismod.",
        "Donec sed odio dui. Nulla vitae elit libero.",
        "Fusce dapibus, tellus ac cursus commodo.",
        "Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis.",
        "Vestibulum id ligula porta felis euismod semper.",
        "Curae; integer lacinia sollicitudin massa."
    ]

    def __init__(self, command):
        self.command = command

    def execute(self):
        for book in self.BOOKS_SAMPLE:
            obj, created = Book.objects.get_or_create(
                title=book["title"],
                defaults={"author": book["author"]}
            )
            if created:
                self.command.stdout.write(self.command.style.SUCCESS(f"Book created: {book['title']}"))
            else:
                self.command.stdout.write(self.command.style.WARNING(f"Book already exists: {book['title']}"))

            if not obj.pages:
                self.create_pages(obj)

        self.command.stdout.write(self.command.style.SUCCESS("Database successfully populated."))

    def create_pages(self, book):
        try:
            sample_number = 10
            content_sample = random.sample(self.BOOKS_CONTENT, sample_number)
            pages = [
                Page(
                    book=book,
                    number=i + 1,
                    content=content_sample[i]
                )
                for i in range(sample_number)
            ]
            Page.objects.bulk_create(pages)
            self.command.stdout.write(self.command.style.SUCCESS(f"{len(pages)} pages created for '{book.title}'"))
        except Exception as e:
            self.command.stdout.write(self.command.style.ERROR(f"Error creating pages for '{book.title}': {e}"))


class Command(BaseCommand):
    help = 'Populates the database with sample book data'

    def handle(self, *args, **kwargs):
        SeedBooksManager(self).execute()

