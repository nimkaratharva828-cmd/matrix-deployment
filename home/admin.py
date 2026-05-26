from django.contrib import admin
from home.models import thumb

class home1(admin.ModelAdmin):
    list_display=('title' , 'dinak','thumbnail_image','id')


admin.site.register(thumb,home1)
# Register your models here.
