from django.contrib import admin
from webo.models import thumb_webo

class hume1_webo(admin.ModelAdmin):
    list_display=('title' , 'dinak','thumbnail_image','id')


admin.site.register(thumb_webo,hume1_webo)

# Register your models here.