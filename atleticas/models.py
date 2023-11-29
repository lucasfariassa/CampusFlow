from django.db import models
from django.contrib.auth.models import User

class Atletica(models.Model):
    USER_TIPO = 'ATL'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_atletica = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='static/images/logos_atleticas', default='static/images/global/logo_atletica_default.png')
    tipo_usuario = models.CharField(max_length=3, default=USER_TIPO)

    class Meta:
        verbose_name = 'Atlética'
        verbose_name_plural = 'Atléticas'
    