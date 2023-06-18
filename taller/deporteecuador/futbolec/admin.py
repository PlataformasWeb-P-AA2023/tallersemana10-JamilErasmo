from django.contrib import admin
from .models import Equipo, Jugador, Campeonato, Campeonatoequipo

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'siglas', 'username')
    search_fields = ('nombre', 'siglas')

admin.site.register(Equipo, EquipoAdmin)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'posicion', 'camiseta', 'sueldo', 'equipo')
    search_fields = ('nombre', 'camiseta')

admin.site.register(Jugador, JugadorAdmin)

class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombausp')
    search_fields = ('nombre',)

admin.site.register(Campeonato, CampeonatoAdmin)

class CampeonatoequipoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'campeonato', 'anio')
    search_fields = ('equipo', 'campeonato')

admin.site.register(Campeonatoequipo, CampeonatoequipoAdmin)
