from django.db import models
import base64
import imghdr
from io import BytesIO
from PIL import Image as PILImage
from django.core.files.base import ContentFile

# Create your models here.

class favourite(models.Model):
    username = models.CharField(max_length=300)
    portfolio = models.CharField(max_length=300)
    productName = models.CharField(max_length=300)
    action = models.BooleanField(default= True)
    orgName = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/', null=True)
    image_url = models.URLField(null=True)
    def __str__(self):
        return self.productName
    
class FavouriteImage(models.Model):
    session_id = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    image = models.TextField()

    def __str__(self):
        return self.username