from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import the custom user model


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser  # Use the custom user model here
        fields = ['username', 'email', 'password1', 'password2']  # Include the email field

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.lower().endswith('@lopesan.com'):
            raise forms.ValidationError("This E-Mail is not allowed.")
        return email
