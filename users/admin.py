# admin.py
from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user_first_name', 'approval',) # Fields to display in the admin list
    list_filter = ('approval',)  # Filter options based on approval field

    def user_first_name(self,obj):
        return obj.user.first_name+" "+obj.user.last_name
admin.site.register(Profile, ProfileAdmin)
