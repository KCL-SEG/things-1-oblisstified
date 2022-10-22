from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

class Thing(models.Model):
    name = models.CharField(unique = True, blank = False, max_length = 30)
    description = models.CharField(unique = False, blank = False, max_length = 120)
    quantity = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(100)])
