from django.db import models

# Create your models here.
class Api(models.Model):
    name = models.CharField(max_length=16, unique=True)
    
    def __str__(self):
        return self.name