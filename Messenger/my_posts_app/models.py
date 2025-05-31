from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class User_Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 205)
    topic = models.CharField(max_length = 150)
    tags = models.JSONField()
    text = models.TextField()
    links = models.JSONField()
    views = models.IntegerField()
    likes = models.IntegerField()

    def get_absolute_url(self):
        return reverse('image_post', kwargs= {'pk': self.pk})
    
class Images_Post(models.Model):
    image = models.ImageField(upload_to= "images/")
    post = models.ForeignKey(User_Post, on_delete=models.CASCADE)