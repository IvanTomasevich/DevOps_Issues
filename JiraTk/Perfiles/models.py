from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    email = models.EmailField()
    cel_phone = models.CharField(max_length=12)

