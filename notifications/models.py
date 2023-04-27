from django.db import models

# Create your models here.


class Noftification(models.Model):
    username = models.CharField(max_length=300)
    portfolio = models.CharField(max_length=300)
    productName = models.CharField(max_length=300)
    companyId = models.CharField(max_length=300, null=True)
    orgName = models.CharField(max_length=300)
    title = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    link = models.CharField(max_length=2048, blank=True, null=True)
    duration = models.CharField(max_length=300, null=True)
    seen = models.BooleanField(default=False)
    button_status = models.CharField(max_length=300, blank=True, null=True)
    document_id = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f'{self.username}'


class Notification(models.Model):
    company_id = models.CharField(max_length=255)
    org_id = models.CharField(max_length=255)
    data_type = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)
    from_field = models.CharField(max_length=255)
    to = models.CharField(max_length=255)
    desc = models.TextField()
    org_name = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    meant_for = models.CharField(max_length=255)
    flag = models.BooleanField()
    type_of_notification = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.org_name}'
