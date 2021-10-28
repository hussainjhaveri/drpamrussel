from django import forms

from .models import Form


class Form1(forms.Form):
    name = forms.CharField(label=' ', required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(label=' ', required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    message = forms.CharField(label=' ', required=True, widget=forms.Textarea(attrs={'placeholder': 'Message'}))
    subject = forms.CharField(label=' ', required=True, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
