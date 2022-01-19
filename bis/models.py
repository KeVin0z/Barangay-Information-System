from django.db import models
from datetime import datetime

class Resident(models.Model):
    full_name = models.CharField(max_length=30)
    nick_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    gender = models.CharField(max_length=30)
    civil_status = models.CharField(max_length=30)
    purok = models.CharField(max_length=30)
    voter_status = models.CharField(max_length=30)

    @property
    def age(self):
        return int((datetime.now().date() - self.birth_date).days / 365.25)

class Official(models.Model):
    full_name = models.CharField(max_length=30)
    chairmanship = models.CharField(max_length=30)
    position = models.CharField(max_length=30)

class Blotter(models.Model):
    complainant = models.CharField(max_length=30)
    respondent = models.CharField(max_length=30)
    victim = models.CharField(max_length=30)
    types = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=30)
    details = models.CharField(max_length=30)

class Sk(models.Model):
    full_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)