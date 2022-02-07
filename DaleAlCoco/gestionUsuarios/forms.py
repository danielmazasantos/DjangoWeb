from django import forms
from django.contrib.auth.models import User


#Formularios implementados encargados de recibir 
#elementos por parametros y enviarlos

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')

class SignupForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput())
        password2 = forms.CharField(widget=forms.PasswordInput())
        class Meta:
            model = User
            fields = ('username', 'password','password2')
