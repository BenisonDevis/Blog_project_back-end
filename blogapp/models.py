from django.db import models

# Create your models here.

class Blog(models.Model):
    heading = models.CharField(max_length = 100)
    description = models.TextField()
    created_at = models.DateField(auto_now = True)
    

