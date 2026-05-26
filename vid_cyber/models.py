# from django.db import models
# from tinymce.models import HTMLField


# class Video(models.Model):
#     title = models.CharField(max_length=255)  # Title of the video
#     video_file = models.FileField(upload_to="vid/")  # Video file upload
#     date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the video is uploaded
#     text = models.TextField()  # Description or text related to the video
#     image = models.ImageField(upload_to="photo/", null=True, blank=True)  # Optional thumbnail or image associated with the video

#     def __str__(self):
#         return self.title

# # Create your models here.

from django.db import models
from tinymce.models import HTMLField  # Import HTMLField from tinymce

class Video_cyber(models.Model):
    title = models.CharField(max_length=255)  # Title of the video
    video_file = models.FileField(upload_to="vid/")  # Video file upload
    date = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the video is uploaded
    text = HTMLField()  # Description or text related to the video (with TinyMCE editor)
    image = models.ImageField(upload_to="photo/", null=True, blank=True)  # Optional thumbnail or image associated with the video

    def __str__(self):
        return self.title

