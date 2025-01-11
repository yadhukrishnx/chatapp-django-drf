from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=128)
    tokens = models.IntegerField(default=4000)
    
    def __str__(self):
        return self.username
    
    