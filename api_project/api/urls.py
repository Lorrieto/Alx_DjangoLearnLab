from django.urls import path
from .views import BookList  # ✅ Import the view

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # ✅ Correct mapping
]