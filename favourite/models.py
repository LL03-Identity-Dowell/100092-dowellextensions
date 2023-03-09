from django.db import models

# Create your models here.

class favourite(models.Model):
    username = models.CharField(max_length=300)
    portfolio = models.CharField(max_length=300)
    productName = models.CharField(max_length=300)
    action = models.BooleanField(max_length=300, null= True)
    orgName = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/', null=True)
    image_url = models.URLField(null=True)
    def __str__(self):
        return self.productName
    