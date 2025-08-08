from django.db import models
from django.utils import timezone

# Author model: stores the name of the author
class Author(models.Model):
    name = models.CharField(max_length=255)  # e.g., "J.K. Rowling"

    def __str__(self):
        return self.name


# Book model: stores details of each book
class Book(models.Model):
    title = models.CharField(max_length=255)  # e.g., "Harry Potter"
    publication_year = models.IntegerField()  # e.g., 1997
    author = models.ForeignKey(
        Author,
        related_name='books',  # lets us access author's books with author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


# Create your models here.
