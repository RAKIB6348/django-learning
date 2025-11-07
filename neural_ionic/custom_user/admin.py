from django.contrib import admin
from custom_user.models import *

# Register your models here.
class Display_Custom_User_List(admin.ModelAdmin):
    list_display = ['username', 'UserType', 'display_name']


admin.site.register(CustomUserModel, Display_Custom_User_List)
