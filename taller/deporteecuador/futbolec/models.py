from django.db import models

class Equipo(models.Model):
    nombre = models.CharField('Nombre del equipo', max_length=40)
    siglas = models.CharField(max_length=30)
    username = models.CharField('Usuario de Twitter', max_length=30)
    campeonatos = models.ManyToManyField('Campeonato', through='Campeonato_equipo')

    def __str__(self):
        return "Nombre: %s - Siglas: %s - Twitter: %s" % (self.nombre, self.siglas, self.username)


class Jugador(models.Model):
    nombre = models.CharField('Nombre Jugador', max_length=40)
    posicion = models.CharField(max_length=50)
    camiseta = models.IntegerField('Numero de camiseta')
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")

    def __str__(self):
        return "Nombre: %s - Posición: %s - Camiseta: %s - Sueldo: %s" % (self.nombre, self.posicion, self.camiseta, self.sueldo)


class Campeonato(models.Model):
    nombre = models.CharField('Nombre del campeonato', max_length=50)
    nombreausp = models.CharField('Nombre del auspiciante', max_length=50)
    equipos = models.ManyToManyField(Equipo, through='Campeonato_equipo')

    def __str__(self):
        return "Nombre: %s - Auspiciante: %s" % (self.nombre, self.nombreausp)


class Campeonatoequipo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    anio = models.IntegerField()

    def __str__(self):
        return "Equipo: %s - Campeonato: %s - Año: %s" % (self.equipo, self.campeonato, self.anio)
