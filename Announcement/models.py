from django.db import models


class Announcement(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
