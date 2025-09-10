from django.db import models

PLATFORM_CHOICES = [
    ("instagram", "Instagram"),
    ("tiktok", "TikTok"),
    ("linkedin", "LinkedIn"),
    ("blog", "Blog"),
    ("x", "X (Twitter)"),
    ("other", "Other"),
]

class Batch(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ContentItem(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="items")
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    media = models.FileField(upload_to="content_media/", blank=True, null=True)  # optional media
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, default="other")
    scheduled_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title or 'Untitled'} — {self.get_platform_display()}"
