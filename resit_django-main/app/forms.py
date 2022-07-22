from .models import Customer
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from .models import Profile
from django.forms import ModelForm


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}

class LoginForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'onfocus': "this.value=''", 'class': 'form-control', 'placeholder': 'Enter Your Username'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'onfocus': "this.value=''", 'class': 'form-control', 'placeholder': 'Enter Your Password'}))

class CustomerAddressForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'address', 'city', 'province', 'zipcode']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),"email":forms.EmailInput(
            attrs={'class': 'form-control'}), 'address': forms.TextInput(attrs={'class': 'form-control'}), 'city': forms.TextInput(
            attrs={'class': 'form-control'}), 'province': forms.Select(attrs={'class': 'form-control'}), 'zipcode': forms.NumberInput(attrs={'class': 'form-control'})}

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}))

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=('Email'), max_length=254, widget=forms.EmailInput(
        attrs={'autocomplete': 'email', 'class': 'form-control'}))

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control'}))

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'username']
