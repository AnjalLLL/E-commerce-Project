from django.contrib import admin
from django.contrib import admin
from .models import UserDetails

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'address','phone','gender', 'joined_date')
    search_fields = ('full_name', 'email')
    readonly_fields = ('joined_date',)

admin.site.register(UserDetails, UserDetailsAdmin)
