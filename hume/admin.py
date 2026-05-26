from django.contrib import admin
from hume.models import thumb

class hume1(admin.ModelAdmin):
    list_display=('title' , 'dinak','thumbnail_image','id')


admin.site.register(thumb,hume1)
# Register your models here.
