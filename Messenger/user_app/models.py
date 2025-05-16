from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class RegistrationCodes(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6)