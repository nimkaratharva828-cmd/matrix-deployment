from django.contrib import admin
from vid_aiml.models import Video_aiml

class video_ai(admin.ModelAdmin):
    list_display=('title' , 'video_file','date','image','id')


admin.site.register(Video_aiml,video_ai)
# Register your models here.
