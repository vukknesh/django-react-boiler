from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import Group

# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_teacher', 'is_student', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_supperuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_teacher', 'is_student', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )

    list_display = ['email', 'username', 'is_teacher', 'is_student']
    search_fields = ('email', 'username')
    ordering =('email',)

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
