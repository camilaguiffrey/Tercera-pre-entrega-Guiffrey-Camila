from django.db import models

from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Alojamiento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ciudad = models.CharField(max_length=200, default="No determinado")
    direccion = models.CharField(max_length=200, default="No determinado")
    email = models.EmailField(default="example@example.com")    
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imagen = models.ImageField(upload_to='alojamiento/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Review(models.Model):
    alojamiento = models.ForeignKey(Alojamiento, on_delete=models.CASCADE)
    texto = models.TextField()
    calificacion = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reseña de {self.usuario} para {self.alojamiento}"