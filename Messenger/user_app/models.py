
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomAbstractUser(AbstractUser):
    avatar = models.ImageField(upload_to='images/', blank=True, null=True, default='images/ranalda.jpg')
    tag_name = models.CharField(max_length = 50, null = True, blank = True)
    birthday = models.DateField(auto_now_add= True, null = True, blank = True)
    request_friends = models.JSONField(null= True, blank= True)
    signature = models.ImageField(upload_to = "images/", null = True, blank = True)
    friends = models.ManyToManyField('self', symmetrical=True, blank=True)

class RegistrationCodes(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6)