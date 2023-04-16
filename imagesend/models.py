from django.db import models

# Create your models here.
class SendImage(models.Model):
    image = models.ImageField(upload_to="images/")
    text = models.CharField(max_length=200)