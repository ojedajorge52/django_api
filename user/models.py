from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField (max_length=50, primary_key=True)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name