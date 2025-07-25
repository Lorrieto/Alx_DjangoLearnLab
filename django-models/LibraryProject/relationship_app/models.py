from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(mx_length=50)
    books = models.ManyToManyField(Book, related_name='library')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)


