from django.contrib import admin
from videos.models import Video

class video1(admin.ModelAdmin):
    list_display=('title' , 'video_file','date','image','id')


admin.site.register(Video,video1)
# Register your models here.
