
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from userapp.models import Users
from candidate.models import Candidates


@staff_member_required
def users(request):
    users = Users.objects.all()
    return render(request, 'user_home.html', {'users': users})

@staff_member_required
def candidates(request):
    candidates = Candidates.objects.all()
    return render(request, 'cand_home.html', {'candidates': candidates})
