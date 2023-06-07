from django.db import models

# Create your models here.

class Common(models.Model):
    created_by = models.CharField(max_length=300)
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    company_id = models.CharField(max_length=300, null=True)
    org_name = models.CharField(max_length=300)
    org_id = models.CharField(max_length=255)

    class Meta:
        abstract = True

class ProductNotification(Common):
    portfolio = models.CharField(max_length=300)
    product_name = models.CharField(max_length=300)
    title = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    link = models.CharField(max_length=2048, blank=True, null=True)
    duration = models.CharField(max_length=300, null=True)
    button_status = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'{self.username}'


class Notification(Common):
    data_type = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)
    from_field = models.CharField(max_length=255)
    to = models.CharField(max_length=255)
    desc = models.TextField()
    org_name = models.CharField(max_length=255)
    meant_for = models.CharField(max_length=255)
    type_of_notification = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.org_name}'
