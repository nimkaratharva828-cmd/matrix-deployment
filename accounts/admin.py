from django.contrib import admin
from accounts.models import User

class jhendu(admin.ModelAdmin):
    list_display=('username' , 'email','password')


admin.site.register(User,jhendu)
# Register your models here.
