
from django import forms
from django.forms import Widget
from django.utils.safestring import mark_safe
from donation.models import Donation
import json
import requests

# resCountry = requests.get("http://battuta.medunes.net/api/country/all/?key=bf52beebb1eb14a75f4894fb8f717336")

# response = json.loads(resCountry.text)
# print(response)

# country_choices = []

# for x in response:
#     country_choices.append((x["code"],x["name"]))




class ChoiceFieldNoValidation(forms.ChoiceField):
    def validate(self, value):
        pass


class DonationForm(forms.ModelForm):
    amount = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'other amount'}))
    # country = forms.ChoiceField(required=True, choices=country_choices)
    region = forms.CharField(required=True, widget=forms.Select(choices=[]))
    hopes = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':50, 'placeholder':'Your hopes for this donation'}))
    donate_for_someone = forms.BooleanField(required=False)
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'John Doe'}), required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '0858XXXXXXXX'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}), required=False)
    payment = forms.ImageField(required=True)

    class Meta:
        model = Donation
        fields = ('amount', 'country', 'region', 'hopes', 'donate_for_someone', 'name', 'phone', 'email', 'payment')
    

    # # excluding field region because cant explicitly state choices
    # def clean(self):
    #     cleaned_data = super(DonationForm, self).clean()

    #     if "region" in self._errors:
    #         del self._errors["region"]
    
    #     return cleaned_data


    
