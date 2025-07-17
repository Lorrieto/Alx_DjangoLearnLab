\#CREATE

from bookshelf.models import Book

book= Book.objects.create(title="1984")



\#RETRIEVE

print(book.title)

1984

print(book.author)

George Orwell

print(book.year)

1949



\#UPDATE

book = Book.objects.get(title="1984")

book.title = "Nineteen Eighty-Four"

book.save()

\# Output: Title updated successfully



\#DELETE

book = Book.objects.get(title="Nineteen Eighty-Four")

book.delete()

Book.objects.all()

\# Output: <QuerySet \[]>

