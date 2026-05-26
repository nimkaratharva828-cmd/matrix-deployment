from django.contrib import admin
from aimlo.models import thumb_aimlo

class hume1_aimlo(admin.ModelAdmin):
    list_display=('title' , 'dinak','thumbnail_image','id')


admin.site.register(thumb_aimlo,hume1_aimlo)

# Register your models here.