import json
from django.shortcuts import render
from donation.models import Person
from donation.forms import DonationForm
from django.http import  JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def show_donation(request):
    context = { 'form': DonationForm() }

    return render(request, "donation.html", context)

@login_required(login_url='/')
def submit_donation(request):
    # form = DonationForm(request.POST or None)

    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)

        if form.is_valid():  

            obj = form.save(commit=False)
            # only create person object when the checkbox is checked
            donate_for_someone = form.cleaned_data['donate_for_someone']
            if donate_for_someone:
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                person_instance = Person(name=name, phone=phone, email=email) 
                person_instance.save()  
            else:
                person_instance = None


            print(person_instance)
            obj.person = person_instance
            obj.save()


            user = request.user

            # the request response
            data = {
            "message": 'Successfully submitted',
            "coin" : '0'
            }
        
            json_object = json.dumps(data, indent = 4) 

            return JsonResponse(json.loads(json_object))
        else:
            # for debugging purposes
            data = {
            "message": form.errors.as_json()
            }
        
            json_object = json.dumps(data, indent = 4) 

            return JsonResponse(json.loads(json_object))


