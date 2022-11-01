import datetime
import json

from django.shortcuts import render, redirect
from donation.models import Donation, Person
from donation.forms import DonationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from django.template import RequestContext

# Create your views here.

def show_donation(request):
    context = { 'form': DonationForm() }

    return render(request, "donation.html", context)

def submit_donation(request):
    # form = DonationForm(request.POST or None)

    print(request.method)
    if request.method == 'POST':
        # bodyRequest = json.loads(request.body.decode("utf-8"))
        # bodyRequest2 = request.POST

        form = DonationForm(request.POST, request.FILES)
        # print(form)
        # print(form.data)
        # print(form.data['region'])


        if form.is_valid():  
 
            # amount = int(form.cleaned_data['amount'])
            # country = form.cleaned_data['country']
            # # not using cleaned data because cant explicitly declare choices in forms.py
            # region = form.data['region']
            
            # donate_for_someone = form.cleaned_data['donate_for_someone']
            
            # hopes = form.cleaned_data['hopes']

            obj = form.save(commit=False)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            person_instance = Person(name=name, phone=phone, email=email) 
            person_instance.save()

            print(person_instance)
            obj.person = person_instance
            obj.save()




            # raise error for empty region (possible case)

            # if region==None or region=="":
            #     data = {
            #     "message": 'Invalid region'
            #     }
            
            #     json_object = json.dumps(data, indent = 4) 

            #     return JsonResponse(json.loads(json_object))

            # Person_instance = None

            # if donate_for_someone==True :

            #     Person_instance = Person(name=name, phone=phone, email=email)
            #     Person_instance.save()

            user = request.user

            # TODO : BELOM ADA IMPLEMENTASI KOINN UNTUK USER
            
            # BELOM ADA USER
            # Donation_instance = Donation(amount=amount, region=region, country=country, hopes=hopes, person=Person_instance, donate_for_someone=donate_for_someone)
            # Donation_instance.save()

            data = {
            "message": 'Successfully submitted',
            "coin" : '0'
            }
        
            json_object = json.dumps(data, indent = 4) 

            return JsonResponse(json.loads(json_object))
        else:
            data = {
            "message": form.errors.as_json()
            }
        
            json_object = json.dumps(data, indent = 4) 

            return JsonResponse(json.loads(json_object))



def get_donations_json(request):
    data = Donation.objects.all()
    return HttpResponse(serializers.serialize('json', data))

