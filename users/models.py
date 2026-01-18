from django.db import models
from django.utils import timezone 

class UserProfile(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.name