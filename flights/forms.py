from django import forms
from django.contrib.auth.models import User
from Core.models import UserProfile

CABIN_CHOICES = [
    ('1','Economy'),
    ('2','Business'),
    ('3', 'First'),
]
class Search(forms.Form):
    source = forms.CharField(label="From:", max_length = 255,widget=forms.TextInput(attrs={'placeholder': 'SFO, LAX, JFK, etc'}))
    destination = forms.CharField(label="To:", max_length = 255,widget=forms.TextInput(attrs={'placeholder': 'SFO, LAX, JFK, etc'}))
    adults = forms.IntegerField(label="No. adults:",initial=1)
    depart = forms.DateField(label="Depart Date:", widget=forms.widgets.DateInput(attrs={'type': 'date'}))
