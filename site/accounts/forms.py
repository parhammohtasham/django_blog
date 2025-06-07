from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm , AdminUserCreationForm

class CustomAdminUserCreationForm(AdminUserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','email','age']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=['username','email','age']