from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'username',
        'first_name',
        'balance',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + (('Balans', {'fields': ('balance',)}),)
    add_fieldsets = UserAdmin.add_fieldsets
    list_per_page = 20


admin.site.register(CustomUser, CustomUserAdmin)
