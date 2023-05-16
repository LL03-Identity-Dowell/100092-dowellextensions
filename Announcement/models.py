from django.db import models


class Announcement(models.Model):
    MEMBER_TYPE_CHOICES = (
        ('Public', 'Public'),
        ('Member', 'Member'),
        ('User', 'User'),
    )
    member_type = models.CharField(max_length=10, choices=MEMBER_TYPE_CHOICES)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    company_id = models.CharField(max_length=255)
    created_at_position = models.CharField(max_length=255)
