from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Add filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields for filtering
    filterset_fields = ['title', 'author', 'published_date']  # Users can filter like ?title=Python

    # Fields for searching (text search)
    search_fields = ['title', 'author']  # Users can search like ?search=Python

    # Fields for ordering
    ordering_fields = ['title', 'published_date']  # Users can order like ?ordering=title or ?ordering=-published_date
    ordering = ['title']  # Default ordering
class BookListView(generics.ListAPIView):
    """
    GET /api/books/

    Features:
    - Filtering: ?title=<title>&author=<author>&published_date=<YYYY-MM-DD>
    - Search: ?search=<text>  (searches title and author)
    - Ordering: ?ordering=<field>  (use '-' prefix for descending)
    """
