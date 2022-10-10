from django.db import models

# Create your models here.


class Autor(models.Model):
    class Meta:
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    def __str__(self):
        return self.apellido, self.nombre


class Libro(models.Model):
    class Meta:
        verbose_name_plural = "Libros"

    titulo = models.CharField(max_length=30)
    genero = models.CharField(max_length=30)
    publicacion = models.DateField(null=True)

    def __str__(self):
        return self.titulo, self.genero, self.publicacion


class Editorial(models.Model):
    class Meta:
        verbose_name_plural = "Editorial"

    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
