# admin.py

from django.contrib import admin

from candidate.models import Candidates, SignUP_cand

from userapp.models import Users, Signup, Register

admin.site.register(Candidates)
admin.site.register(Users)
admin.site.register(Register)
admin.site.register(Signup)
admin.site.register(SignUP_cand)
