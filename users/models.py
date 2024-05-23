from django.db import models

class User(models.Model):
    
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)