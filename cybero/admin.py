from django.contrib import admin
from cybero.models import thumb_cybero

class hume1_cybero(admin.ModelAdmin):
    list_display=('title' , 'dinak','thumbnail_image','id')


admin.site.register(thumb_cybero,hume1_cybero)

# Register your models here.