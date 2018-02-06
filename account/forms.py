from django import forms
from django.forms import ModelForm
from django.conf import settings
from account.models import Person, Labor

class UserLoginForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput) #(attrs={'class': 'sr-only'}))
    #email = forms.CharField(label='Email Address', widget=forms.EmailField) #(attrs={'class': 'form-control'}))
    
    class Meta:
        
        model = Labor
        fields = ('laborcode',)