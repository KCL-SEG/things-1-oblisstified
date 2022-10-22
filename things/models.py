from django.db.models import Model,IntegerField
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(Model):
    name = CharFirld(unique = False, blank = False, max_length = 30)
    description = CharFirld(unique = False, blank = False, max_length = 200)
    quantity = IntegerField(validators = [MinValueValidator(0),MaxValueValidator(100)])
