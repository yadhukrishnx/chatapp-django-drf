from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    tokens = models.IntegerField(default=4000)
    
    def __str__(self):
        return self.username
    
    