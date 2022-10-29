from django import forms

import json
import requests

resCountry = requests.get("http://battuta.medunes.net/api/country/all/?key=e156eb48631da358df83b2219d80585d")

response = json.loads(resCountry.text)
print(response)

country_choices = []

for x in response:
    country_choices.append((x["code"],x["name"]))



class DonationForm(forms.Form):
    field_amount = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'Your desired amount'}))
    field_country = forms.ChoiceField(required=True, choices=country_choices)
    field_region = forms.ChoiceField(required=True)
    field_hopes = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':50, 'placeholder':'Your hopes for this donation'}))
    checkbox_donate_for_someone = forms.BooleanField(required=False)
    field_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'John Doe'}), required=False)
    field_phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '0858XXXXXXXX'}), required=False)
    field_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}), required=False)
    

    # excluding field region because cant explicitly state choices
    def clean(self):
        cleaned_data = super(DonationForm, self).clean()

        # ignore 'len' when 'check' is False
        if "field_region" in self._errors:
            del self._errors["field_region"]
    
        return cleaned_data

    
