from django.shortcuts import render, redirect


def home(request):
    return render(request, 'homepage.html')



def admin_view(request):
    return redirect(request, 'Admin')


def candidate_portal(request):
    return render(request, 'cand_home.html')


def user_portal(request):
    return render(request,'user_home.html')


