from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', views.admin_view, name='admin'),
    path('User/', views.user_portal, name='user_portal'),
    path('candidates/', views.candidate_portal, name='candidates_portal'),


 ]







