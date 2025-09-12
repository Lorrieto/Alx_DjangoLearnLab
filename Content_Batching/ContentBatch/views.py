from django.shortcuts import render, get_object_or_404, redirect
from .models import Batch, ContentItem
from .forms import BatchForm, ContentItemForm

def batch_list(request):
    batches = Batch.objects.all()
    return render(request, "content/batch_list.html", {"batches": batches})

def batch_detail(request, batch_id):
    batch = get_object_or_404(Batch, id=batch_id)
    items = batch.items.all()
    return render(request, "content/batch_detail.html", {"batch": batch, "items": items})

def batch_create(request):
    if request.method == "POST":
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("batch_list")
    else:
        form = BatchForm()
    return render(request, "content/batch_form.html", {"form": form})

def contentitem_create(request, batch_id):
    batch = get_object_or_404(Batch, id=batch_id)
    if request.method == "POST":
        form = ContentItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.batch = batch
            item.save()
            return redirect("batch_detail", batch_id=batch.id)
    else:
        form = ContentItemForm()
    return render(request, "content/contentitem_form.html", {"form": form, "batch": batch})
