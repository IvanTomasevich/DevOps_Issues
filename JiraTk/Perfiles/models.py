from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return f"Perfil de: {self.user_profile}"
