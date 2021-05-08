from django.forms import ModelForm
from django import forms
from django.forms import ModelChoiceField
from .models import *


class query_form(forms.ModelForm):
    class Meta:
        model = query
        fields = ['query_name', 'query_email', 'query_contact', 'query_desc']

        query_desc = forms.Nu