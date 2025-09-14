from django.contrib import admin
from .models import Batch, ContentItem

class ContentItemInline(admin.TabularInline):
    model = ContentItem
    extra = 1
    fields = ("title", "platform", "scheduled_date", "media")

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name", "description")
    inlines = [ContentItemInline]

@admin.register(ContentItem)
class ContentItemAdmin(admin.ModelAdmin):
    list_display = ("title", "platform", "batch", "scheduled_date", "created_at")
    list_filter = ("platform", "scheduled_date")
    search_fields = ("title", "body", "notes")
