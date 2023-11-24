from django.contrib import admin
from .models import Atletica

class AtleticaAdmin(admin.ModelAdmin):
    list_display = ('nome_atletica', 'logo')
admin.site.register(Atletica)
