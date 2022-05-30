from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import *

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields=['name','email','password']
