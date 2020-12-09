from django.db import models

# Create your models here.

class Post(models.Model):
    titel = models.CharField(max_length=150)
    desc = models.TextField()


