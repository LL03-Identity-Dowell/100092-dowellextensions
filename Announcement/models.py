from django.db import models


class Announcement(models.Model):
    MEMBER_TYPE_CHOICES = (
        ('Public', 'Public'),
        ('Member', 'Member'),
        ('User', 'User'),
    )
    member_type = models.CharField(max_length=10, choices=MEMBER_TYPE_CHOICES)
    description = models.TextField(max_length=2028)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=255, null=False)
    product_id = models.CharField(max_length=255, null=False)
    created_by = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    org_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255, default="Unknown")
    org_name = models.CharField(max_length=255, default="Unknown")
    created_at_position = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=500)
