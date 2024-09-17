from django.contrib import admin
from userauths.models import User, Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    list_editable = ('phone', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('full_name', 'email')
    list_filter = ['date_joined']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'gender', 'country')
    list_editable = ('gender', 'country')
    search_fields = ('full_name', 'user__email', 'gender', 'country')
    list_filter = ['date']

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)