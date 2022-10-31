from django import forms

import json
import requests

resCountry = requests.get("http://battuta.medunes.net/api/country/all/?key=e156eb48631da358df83b2219d80585d")

response = json.loads(resCountry.text)
print(response)

country_choices = []

for x in response:
    country_choices.append((x["code"],x["name"]))

from django import forms
from django.forms import Widget
from django.utils.safestring import mark_safe

# class PrependWidget(Widget):
#     """ Widget that prepend boostrap-style span with data to specified base widget """

#     def __init__(self, base_widget, data, *args, **kwargs):
#         u"""Initialise widget and get base instance"""
#         super(PrependWidget, self).__init__(*args, **kwargs)
#         self.base_widget = base_widget(*args, **kwargs)
#         self.data = data

#     def render(self, name, value, attrs=None):
#         u"""Render base widget and add bootstrap spans"""
#         field = self.base_widget.render(name, value, attrs)
#         return mark_safe((
#             u'<div class="input-group mb-3">'
#             u'  <div class="input-group-prepend">'
#             u'    <span class="input-group-text" id="basic-addon1">%(data)s</span>'
#             u'  </div>'
#             u'  <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">'
#             u'</div>'
#         ) % {'field': field, 'data': self.data})



class DonationForm(forms.Form):
    field_amount = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'placeholder': 'other amount'}))
    field_country = forms.ChoiceField(required=True, choices=country_choices)
    field_region = forms.ChoiceField(required=True)
    field_hopes = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':50, 'placeholder':'Your hopes for this donation'}))
    checkbox_donate_for_someone = forms.BooleanField(required=False)
    field_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'John Doe'}), required=False)
    field_phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '0858XXXXXXXX'}), required=False)
    field_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}), required=False)
    field_payment = forms.ImageField(required=False)
    

    # excluding field region because cant explicitly state choices
    def clean(self):
        cleaned_data = super(DonationForm, self).clean()

        if "field_region" in self._errors:
            del self._errors["field_region"]
    
        return cleaned_data


    
