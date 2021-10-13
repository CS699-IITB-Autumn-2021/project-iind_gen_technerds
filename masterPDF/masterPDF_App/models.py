from django.db import models

# Create your models here.
class PDF(models.Model):
    pdf_uploaded = models.FileField(upload_to='')
