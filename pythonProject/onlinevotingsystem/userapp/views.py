
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Signup, User,Register


def home(request):
    return render(request, 'user_home.html')

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        if username is not None:
            return render(request, 'user_home.html')
        else:
            return "Username is missing in the form data."
    else:
        return render(request, 'user_login.html')


def results(request):
    return render(request, "user_results.html")


def register(request):
    if request.method == 'POST':
        fullname = request.POST('fullname')
        aadhar = request.POST('aadhaar')
        qualification = request.POST('qualification')
        mobile = request.POST('mobile')
        birth_date = request.POST('birth_date')
        gender = request.POST('gender')
        address = request.POST('address')
        country = request.POST('country')
        city = request.POST('city')
        region = request.POST('region')
        postalcode = request.POST('postalcode') 

    
        
        us = Register(fullname=fullname,aadhar=aadhar,mobile=mobile,qualification=qualification,birth_date=birth_date,gender=gender,
            address=address,address1=address1,country=country,city=city,region=region,postalcode=postalcode)
        us.save()
             
        return redirect('home')

    return render(request, 'user_register.html')

def voting(request):
    return render(request, 'user_voting.html')




def signup(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            s = Signup(uid=uid,email=email, password=password)
            Signup.save(s)
            msg = 'Registration is Successful'

            return render(request, 'user_login.html', {'msg': msg})
        else:
            msg = 'Password is different'
            return render(request, 'user_signup.html', {'msg1': msg})

    return render(request,"user_signup.html")


def usercandidate(request):
    return render(request, 'user_candidate.html')


def vote(request):
    party_id = request.POST.get('party_id')
    party = Party.objects.get(id=party_id)
    party.votes += 1
    party.save()
    return JsonResponse({'votes': party.votes})

