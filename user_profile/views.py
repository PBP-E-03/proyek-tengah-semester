import json
from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render

from authentication.models import User
from user_profile.forms import PasswordForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

# Create your views here.
@login_required(login_url='/')
def index(request):
    user = User.objects.filter(pk=request.user.id).first()
    context = {
        "profile_form": ProfileForm(instance = user, auto_id="id_profile_%s"),
        "password_form": PasswordForm(auto_id="id_profile_%s")
    }
    return render(request, 'profile.html', context)

@login_required(login_url='/')
def update_profile(request):
    if request.method == 'POST':
        bodyRequest = json.loads(request.body.decode("utf-8"))
        user = User.objects.get(pk=request.user.id)

        form = ProfileForm(bodyRequest, instance=user)
        if form.is_valid():
            form.save()
            bodyResponse = {
                "success": True,
                "content": None,
                "message": "Successfully updated"
            }
        else:
            print(form.errors)
            bodyResponse = {
                "success": False,
                "content": None,
                "message": "Please recheck your data"
            }
        json_object = json.dumps(bodyResponse, indent = 4) 

        return JsonResponse(json.loads(json_object))
    return HttpResponseNotAllowed(['GET'])

@login_required(login_url='/')
def update_password(request):
    if request.method == 'POST':
        bodyRequest = json.loads(request.body.decode("utf-8"))
        form = PasswordForm(bodyRequest)
        if form.is_valid():
            user = authenticate(request, email=request.user.email, password=form.cleaned_data['current_password'])
            if user is not None:
                user.set_password(form.cleaned_data['new_password'])
                user.save()
                bodyResponse = {
                    "success": True,
                    "content": None,
                    "message": "Successfully updated"
                }
            else:
                bodyResponse = {
                    "success": False,
                    "content": None,
                    "message": "Wrong password"
                }
        else:
            print(form.errors)
            bodyResponse = {
                "success": False,
                "content": None,
                "message": "Please recheck your data"
            }
            
        json_object = json.dumps(bodyResponse, indent = 4) 

        return JsonResponse(json.loads(json_object))
    return HttpResponseNotAllowed(['GET'])
