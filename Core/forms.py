from django import forms
from django.contrib.auth.models import User
from Core.models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
class JoinForm(forms.ModelForm):
    username = forms.CharField(help_text=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
class EditSettings(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'profile_picture']
