from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class thumb(models.Model):
    title=models.CharField(max_length=60)
    dinak=models.DateField()
    thumbnail_image=models.FileField(upload_to="thumbnail/",max_length=250,null=True,default=None)