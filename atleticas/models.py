from django.db import models
from django.contrib.auth.models import User

class Atletica(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_atletica = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='static/logos_atleticas')

    class Meta:
        verbose_name = 'Atlética'
        verbose_name_plural = 'Atléticas'
    