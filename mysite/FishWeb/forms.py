from django import forms

from .models import Form


class Form1(forms.ModelForm):
    name = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(label=' ', required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    message = forms.CharField(label=' ',
                              widget=forms.Textarea(attrs={'placeholder': 'Message', 'cols': 30, 'rows': 1}))
    company = forms.CharField(label=' ', widget=forms.Textarea(attrs={'placeholder': 'Company'}))
    manager = forms.CharField(label=' ', widget=forms.Textarea(attrs={'placeholder': 'Manager'}))
    budget = forms.IntegerField(label=' ', widget=forms.Textarea(attrs={'placeholder': 'Budget'}))

    class Meta:
        model = Form
        fields = '__all__'
