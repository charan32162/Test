from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "users"

    def str(self):
      return self.user.username



class Signup(models.Model):
        uid = models.IntegerField()
        fullname = models.CharField(max_length=100, blank=False)
        email = models.CharField(max_length=100)
        password = models.CharField(max_length=100)

        class Meta:
            db_table =  "user_signup"

class Register(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    aadhaar = models.BigIntegerField(blank=False, unique=True)
    education = (
        ("SSC", "SSC"), ("Intermediate", "Intermediate"), ("U.G", "U.G"), ("P.G", "P.G"), ("Ph.D", "Ph.D"),
        ("None", "None")
    )
    qualification = models.CharField(max_length=100, blank=False, choices=education)
    mobile = models.BigIntegerField(blank=False)
    gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("Prefer Not To Say", "Prefer Not To Say"))
    gender = models.CharField(max_length=20, blank=False, choices=gender_choices)
    birthdate = models.DateField(blank=False)
    address = models.CharField(max_length=100, blank=False)
    address1 = models.CharField(max_length=100, blank=False)
    country_choices = (("INDIA", "INDIA"), ("INDIA", "INDIA"))
    country = models.CharField(max_length=20, blank=False, choices=country_choices)
    city = models.CharField(max_length=30, blank=False)
    region = models.CharField(max_length=20, blank=False)
    postalcode = models.CharField(max_length=6, blank=False)

    class Meta:
        db_table = "register"
