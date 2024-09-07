from django import forms
from .models import Account
from django.core.exceptions import ValidationError

class RegistartionForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=['first_name','last_name','phone_number','email','password']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Account.objects.filter(email=email).exists():
            raise ValidationError("Email ya existe.")
        return email


