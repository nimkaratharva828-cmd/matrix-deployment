from django.contrib import admin
from vid_web.models import Video_web

class video_we(admin.ModelAdmin):
    list_display=('title' , 'video_file','date','image','id')


admin.site.register(Video_web,video_we)
# Register your models here.
