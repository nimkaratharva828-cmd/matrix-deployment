from django.contrib import admin
from vid_cyber.models import Video_cyber

class video_cy(admin.ModelAdmin):
    list_display=('title' , 'video_file','date','image','id')


admin.site.register(Video_cyber,video_cy)
# Register your models here.
