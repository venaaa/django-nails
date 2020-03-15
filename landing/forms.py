from django import forms
from .models import *

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        exclude = ['']
        # widgets = {
        #     'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
        #     'email': forms.TextInput(attrs={'placeholder': 'Your Email'}),
        # }