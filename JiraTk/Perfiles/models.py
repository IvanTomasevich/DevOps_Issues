from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return f"Avatar de: {self.user_profile}"
