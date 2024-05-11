from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["username", "firstname", "lastname", "address","tel_number"]
 
    def username(self, obj):
        return obj.user.username
    
    def firstname(self, obj):
        return obj.user.first_name
    
    def lastname(self, obj):
        return obj.user.last_name
admin.site.register(UserProfile, UserProfileAdmin)
