from django.db import models
from django.contrib.auth.models import User

class Batch(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="batches")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
