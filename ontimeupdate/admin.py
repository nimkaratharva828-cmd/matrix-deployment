from django.contrib import admin
from ontimeupdate.models import upde


class info(admin.ModelAdmin):
    list_display=('title' , 'video_file','date','image','id')

# Register your models here.
admin.site.register(upde,info)