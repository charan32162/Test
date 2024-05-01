from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homepage'),
    path("signup", views.signup, name="signup"),
    path("login", views.cand_Login, name="login"),
    path("Results", views.cand_results, name="Results"),
    path("Candidates", views.candidate, name="Candidates"),
    path("register", views.register, name="register"),
    path("vote", views.vote, name="vote"),
    path('logout', views.logout, name="logout"),

]
