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

# Book API – Filtering, Searching, Ordering

### List Books Endpoint
`GET /api/books/`

#### Filtering:
- Filter by title: `/api/books/?title=Python`
- Filter by author: `/api/books/?author=John Doe`
- Filter by published date: `/api/books/?published_date=2023-01-01`

#### Searching:
- Search in title/author: `/api/books/?search=Python`

#### Ordering:
- Order by title ascending: `/api/books/?ordering=title`
- Order by published_date descending: `/api/books/?ordering=-published_date`
