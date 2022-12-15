from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    bio = models.CharField(max_length=280)
    date_created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title