import json
from django.http import JsonResponse
from django.shortcuts import render
from authentication.forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def registration(request):
    if request.method == 'POST':
        bodyRequest = json.loads(request.body.decode("utf-8"))
        form = RegistrationForm(bodyRequest)
        if form.is_valid():
            form.save()
            bodyResponse = {
                "success": True,
                "content": None,
                "message": "Successfully registered"
            }
        else:
            bodyResponse = {
                "success": False,
                "content": None,
                "message": "Please recheck your data"
            }
            
        json_object = json.dumps(bodyResponse, indent = 4) 

        return JsonResponse(json.loads(json_object))
    
    context = { 'form' : RegistrationForm() }
    return render(request, 'registration.html', context)

def auth_login(request):
    if request.method == 'POST':
        bodyRequest = json.loads(request.body.decode("utf-8"))
        form = LoginForm(bodyRequest)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if not form.cleaned_data['remember_me']:
                    print("expiry",  request.session.get_expire_at_browser_close())
                    request.session.set_expiry(0)
                    print("expiry",  request.session.get_expire_at_browser_close())
                    
                bodyResponse = {
                    "success": True,
                    "content": None,
                    "message": "Login successful"
                }
            else:
                bodyResponse = {
                    "success": False,
                    "content": None,
                    "message": "Email or Password is Invalid!"
                }
            
        else:
            bodyResponse = {
                "success": False,
                "content": None,
                "message": "Please recheck your data"
            }
        
        
        json_object = json.dumps(bodyResponse, indent = 4) 
        return JsonResponse(json.loads(json_object))
    
    context = { 'form' : LoginForm() }
    return render(request, 'login.html', context)

def auth_logout(request):
    logout(request)
    bodyResponse = {
            "success": True,
            "content": None,
            "message": "Successfully logged out"
        }
    json_object = json.dumps(bodyResponse, indent = 4) 
    return JsonResponse(json.loads(json_object))