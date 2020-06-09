from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CITYCHOICE = [
    ('patan', 'PATAN'),
    ('amdavad', 'AMDAVAD'),
    ('vadodara', 'VDODARA'),
    ('surat', 'SURAT')
]

STATECHOICE = [
    ('gujarat', 'GUJARAT'),
    ('maharasra', 'MAHARASTRA'),
    ('rajastan', 'RAJASTHAN')
]


# user address
class Userdetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, default='-')
    pincode = models.CharField(max_length=7, default='384265')
    city = models.CharField(max_length=50, choices=CITYCHOICE, default=('patan', 'PATAN'))
    state = models.CharField(max_length=50, choices=STATECHOICE, default=('gujarat', 'GUJARAT'))
