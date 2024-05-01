from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("LOGIN", views.userLogin, name="LOGIN"),
    path("Register", views.register, name="Register"),
    path("SIGNUP", views.signup, name="SIGNUP"),
    path("results", views.results, name="results"),
    path("voting", views.voting, name="voting"),
    path("candidate", views.usercandidate, name="candidate"),
]