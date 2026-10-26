from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=120)
    business_name = models.CharField(max_length=120)
    description = models.TextField()
    image_url = models.URLField()
    link_url = models.URLField(blank=True)
    category = models.CharField(max_length=60, default="General")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at", "title"]

    def __str__(self):
        return f"{self.title} — {self.business_name}"
