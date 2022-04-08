from django import forms
from django.contrib.auth.models import User
from Core.models import UserProfile
DOLLAR_CHOICES = [
    ('1','$ - Inexpensive'),
    ('2','$$ - Moderately Expensive'),
    ('3','$$$ - Expensive'),
    ('4','$$$$ - Very Expensive'),
]
class Search(forms.Form):
    cuisine = forms.CharField(max_length = 255,widget=forms.TextInput(attrs={'placeholder': 'Chinese, Burgers,etc'}))
    zip_code = forms.CharField(max_length = 5,widget=forms.TextInput(attrs={'placeholder': '94027,90210,etc'}))
    price = forms.CharField(label='Price:', widget=forms.Select(choices=DOLLAR_CHOICES))
