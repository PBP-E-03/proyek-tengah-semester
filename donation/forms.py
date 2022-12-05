
from django import forms
from django.forms import Widget
from django.utils.safestring import mark_safe
from donation.models import DonationHistory
from main.models import Country


class CountryChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name
class DonationHistoryForm(forms.ModelForm):
    amount = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'other amount'}))
    country = CountryChoiceField(required=True, queryset=Country.objects.all(), to_field_name="code", empty_label=None)
    region = forms.CharField(required=True, widget=forms.Select(choices=[]))
    hopes = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':50, 'placeholder':'Your hopes for this donation'}))
    donate_for_someone = forms.BooleanField(required=False)
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'John Doe'}), required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '0858XXXXXXXX'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}), required=False)
    payment = forms.ImageField(required=True)

    class Meta:
        model = DonationHistory
        fields = ('amount', 'country', 'region', 'hopes', 'donate_for_someone', 'name', 'phone', 'email', 'payment')
   

    
