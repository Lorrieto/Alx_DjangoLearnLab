from django.db import models

class Author(models.Model):
    self.name = models.CharField(max_length=50)
    return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

class Library(models.Model):
    name = models.CharField(mx_length=50)
    books = models.ManyToManyField(Book, related_name='library')

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)


