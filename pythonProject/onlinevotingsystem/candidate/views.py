from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate
from .models import SignUP_cand




def home(request):
    return render(request, 'cand_home.html')

def candidate(request):
    return render(request, 'candidate.html')


def cand_results(request):
    return render(request, "results.html")

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        aadhar_number = request.POST.get('aadhar_number')
        qualification = request.POST.get('qualification')
        phone_number = request.POST.get('phone')
        birth_date = request.POST.get('birthdate')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        return redirect('success_page')
    return render(request, 'candidates/register.html')


def cand_Login(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        if username is not None:
            return render(request,'cand_home.html')
        else:
            return "Username is missing in the form data."
    else:
        return render(request, 'cand_login.html')


def vote(request):
    return render(request, "cand_voting.html")

def logout(request):
    logout(request)
    return redirect('homepage')

def signup(request):
    if request.method == "POST":
        id = request.POST["id"]
        full_name = request.POST["full_name"]
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            s = SignUP_cand(username=id, full_name=full_name, email=email, password=password)
            SignUP_cand.save(s)
            msg = 'Registration is Successful'

            return render(request, 'cand_login.html', {'msg': msg})
        else:
            msg = 'Password is different'
            return render(request, 'cand_signup.html', {'msg1': msg})

    return render(request,"cand_signup.html")


