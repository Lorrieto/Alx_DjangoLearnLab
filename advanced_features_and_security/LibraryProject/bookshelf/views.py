from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from bookshelf.models import Article

@permission_required('bookshelf.can_view', raise_exception=True)
def view_article(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_article(request):
    # creation logic
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request, article_id):
    # editing logic
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_article(request, article_id):
    # deletion logic
    pass

# Create your views here.
