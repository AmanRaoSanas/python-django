from django import forms
from .models import User

class userf(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']