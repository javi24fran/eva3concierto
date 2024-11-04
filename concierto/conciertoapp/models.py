from django.db import models

class Persona(models.Model):
    RUT = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    edad = models.PositiveIntegerField()
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Concierto(models.Model):
    conciertoID = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.lugar} - {self.fecha}"

class Entrada(models.Model):
    entradaID = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=50)
    descripcion = models.TextField()
    numero_asiento = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    sector = models.CharField(max_length=50)
    concierto = models.ForeignKey(Concierto, on_delete=models.CASCADE)  # Relación uno a muchos con Concierto
    #cada entrada tiene un concierto asociado, y el campo concierto en Entrada es una clave foránea que apunta a un objeto Concierto.
    #muchas entradas pueden estar relacionadas con un solo concierto (relación uno a muchos).
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)  # Relación uno a muchos con Persona
    #cada entrada está asociada a una persona. Muchas entradas pueden estar relacionadas con una sola persona.

    def __str__(self):
        return f"Entrada {self.entradaID} - {self.categoria}"



# Create your models here.
