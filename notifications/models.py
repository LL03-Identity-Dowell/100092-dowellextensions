from django.db import models

# Create your models here.

class Noftification(models.Model):
    username = models.CharField(max_length=300)
    portfolio = models.CharField(max_length=300)
    productName = models.CharField(max_length=300)
    companyId = models.CharField(max_length=300, null= True)
    orgName = models.CharField(max_length=300)
    title = models.CharField(max_length=500)
    message =models.CharField(max_length=500)
    link = models.CharField(max_length=2048, blank=True, null= True)
    duration = models.CharField(max_length=300, null= True)
    seen = models.BooleanField(default=False)