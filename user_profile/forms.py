from django import forms
from django.forms import ModelForm, ValidationError
from phonenumber_field.formfields import PhoneNumberField


from authentication.models import User


class ProfileForm(ModelForm):
    phone = PhoneNumberField(region="ID", required=True, label="Phone Number", widget=forms.TextInput)
    address = forms.CharField(required=True, label="Address", widget=forms.Textarea)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'address']
        
class PasswordForm(forms.Form):
    current_password = forms.CharField(label="Current Password", widget=forms.PasswordInput(attrs={
        "placeholder": "Your current password"
    }))
    
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={
        "placeholder": "Must have at least 6 characters"
    }))
    
    password_confirmation = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput(attrs={
        "placeholder": "Retype your password"
    }))
    
    def clean(self):
        new_password = self.cleaned_data['new_password']
        password_confirmation = self.cleaned_data['password_confirmation']
        
        if new_password != password_confirmation:
            raise ValidationError("Password doesn't match")
        
        return self.cleaned_data