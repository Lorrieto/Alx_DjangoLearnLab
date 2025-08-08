from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()       # retrieves all Book records
    serializer_class = BookSerializer   # uses our serializer

# Create your views here.
