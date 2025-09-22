from django.contrib import admin
from .models import Pregunta, Opcion

# Registrar los modelos en el admin
admin.site.register(Pregunta)
admin.site.register(Opcion)
