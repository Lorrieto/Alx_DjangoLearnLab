from django import forms
from .models import Batch, ContentItem

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ["name", "description"]

class ContentItemForm(forms.ModelForm):
    class Meta:
        model = ContentItem
        fields = ["title", "body", "media", "platform", "scheduled_date", "notes"]
