from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

class Thing(models.Model):
    name = models.CharFirld(unique = False, blank = False, max_length = 30)
    description = models.CharFirld(unique = False, blank = False, max_length = 200)
    quantity = models.IntegerField(validators = [MinValueValidator(0),MaxValueValidator(200)])
