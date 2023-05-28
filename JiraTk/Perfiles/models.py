from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    email = models.EmailField()
    cel_phone = models.CharField(max_length=12)

    class meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.name} {self.last_name}, Cel:{self.cel_phone}, email:{self.email}"
