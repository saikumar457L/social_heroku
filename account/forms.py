from django import forms

from django.conf import settings
from django.contrib.auth.models import User
from .models import Profile

# from django.contrib.auth import get_user_model

class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label="Password",widget=forms.PasswordInput) # the variable must be with password

    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput) # the variable must be with password2

    class Meta:
        model = User
        fields = ["username","first_name","email"]

    def clean_password2(self): # the clean_password2 must be defined with clean_password2
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:

            raise forms.ValidationError("Passwords don't match try again.")

        return cd['password2']


class UserEditForm(forms.ModelForm):

    class Meta:
            model = User
            fields = ["first_name","email","last_name"]

class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["date_of_birth","photo"]
