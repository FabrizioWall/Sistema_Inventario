from django.contrib import admin

# Register your models here.
from .models import *

class CampaniaAdmin(admin.ModelAdmin):
    list_display = ('nombre_campania', 'descripcion_campania')
    
admin.site.register(Notebook)
admin.site.register(Campania, CampaniaAdmin)
admin.site.register(Periferico)
admin.site.register(Persona)
admin.site.register(Computadora)