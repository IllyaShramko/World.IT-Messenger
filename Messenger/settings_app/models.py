from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length = 100)
    subtitle =  models.CharField(max_length = 100)
    date = models.DateField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

class AlbumImage(models.Model):
    image = models.ImageField(upload_to="images/")
    album = models.ForeignKey(Album, on_delete=models.CASCADE)