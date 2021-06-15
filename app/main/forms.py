from django import forms
from .models import *

class Search(forms.Form):
    starting_point = forms.CharField(max_length=255)
    terminus = forms.CharField(max_length=255)