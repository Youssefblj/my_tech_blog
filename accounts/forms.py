from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    # ✅ Username validation — letters only
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username.isalpha():
            raise forms.ValidationError("Username must contain letters only (no numbers or symbols).")
        return username

    # ✅ Email validation — unique email
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email

    # ✅ Password validation — must contain both letters and numbers
    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$', password):
            raise forms.ValidationError(
                "Password must be at least 6 characters long and contain both letters and numbers."
            )
        return password
