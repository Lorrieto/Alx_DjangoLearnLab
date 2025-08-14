# Book API – DRF Generic Views

## Endpoints:
- GET /api/books/ → List all books (public)
- GET /api/books/<id>/ → Retrieve book details (public)
- POST /api/books/create/ → Create a new book (authenticated)
- PUT/PATCH /api/books/<id>/update/ → Update a book (authenticated, owner only)
- DELETE /api/books/<id>/delete/ → Delete a book (authenticated, owner only)

## Permissions:
- Read is public
- Write requires authentication
- Owner restriction on update/delete

## Search and Ordering:
- Search: /api/books/?search=python
- Order: /api/books/?ordering=title
