from django.contrib import admin
from .forms import CustomUserChangeForm , CustomAdminUserCreationForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form=CustomAdminUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=['username','email','age']

    fieldsets=UserAdmin.fieldsets + (
        (None , {'fields':('age',)}),
    )
    add_fieldsets=UserAdmin.add_fieldsets + (
        (None , {'fields':('age',)}),
    )

admin.site.register(CustomUser , CustomUserAdmin)