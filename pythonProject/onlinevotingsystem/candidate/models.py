from django.db import models

class Candidates(models.Model):
    name = models.CharField(max_length=100, blank=False)
    Age= models.IntegerField(blank=False)
    Gender= models.CharField(max_length=7, blank=False)
    BirthDate= models.DateField(blank=False)
    party= models.CharField(max_length=10, blank=False)

class Meta:
    db_table = "Candidate"

def __str__(self):
    return self.name

class SignUP_cand(models.Model):
        username = models.IntegerField( blank=False)
        full_name = models.CharField(max_length=100, blank=False)
        email = models.CharField(max_length=100)
        password = models.CharField(max_length=100)

        class Meta:
            db_table = "cand_signup"



