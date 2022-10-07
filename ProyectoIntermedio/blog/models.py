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

    título = models.CharField(max_length=30)
    género = models.CharField(max_length=30)
    publicación = models.DateField(null=True)


class Analisis(models.Model):
    class Meta:
        verbose_name_plural = "Análisis"

    texto = models.CharField(max_length=1500)
