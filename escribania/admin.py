from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(ActoJuridico)
class ActoJuridicoAdmin(admin.ModelAdmin):
    pass

@admin.register(Escribano)
class EscribanoAdmin(admin.ModelAdmin):
    pass

@admin.register(Escritura)
class EscrituraAdmin(admin.ModelAdmin):
    pass