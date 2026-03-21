from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email")

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'bio', 'link', 'cumpleanos']
        widgets = {
            'cumpleanos': forms.DateInput(attrs={'type': 'date'}), # Esto pone el calendario
        }