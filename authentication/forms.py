from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import User
from phonenumber_field.formfields import PhoneNumberField

class RegistrationForm(UserCreationForm):
    name = forms.CharField(required=True, label="Name", widget=forms.TextInput(attrs={
        'placeholder': "John Doe"
    }))
    phone = PhoneNumberField(region="ID", required=True, label="Phone Number", widget=forms.TextInput(attrs={
        'placeholder': "0858xxxxxxxxx"
    }))
    address = forms.CharField(required=True, label="Address", widget=forms.Textarea(attrs={
        'placeholder': "Tree Street, 27"
    }))
    
    class Meta:
        model = User
        fields = ('name', 'phone', 'address', 'email')
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': "example@mail.com"
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': "Must have at least 6 characters"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': "Retype your password"})

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput(attrs={
        'placeholder': "example@mail.com"    
    }))
    password = forms.CharField(required=True, label="Email", widget=forms.PasswordInput(attrs={
        'placeholder': "Must have at least 6 characters"    
    })) 
    remember_me = forms.BooleanField(label="Remember Me", required=False)
    
    class Meta:
        model = User