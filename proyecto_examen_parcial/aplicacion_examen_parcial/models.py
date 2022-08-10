from django.db import models

class Libros(models.Model):
    titulo = models.CharField(max_length=100, null=True)
    autor = models.CharField(max_length=100,null=True)
    descripcion = models.CharField(max_length=500,null=True)
    imagen = models.FileField(upload_to='libros/',null=True,verbose_name="")
    def __str__(self):
        return self.titulo + ":" + str(self.imagen)

class Canciones(models.Model):
    titulo = models.CharField(max_length=100, null=True)
    banda = models.CharField(max_length=100, null=True)
    album = models.CharField(max_length=100, null=True)
    imagen = models.FileField(upload_to='canciones/',null=True,verbose_name="")
    def __str__(self):
        return self.titulo + ":" + str(self.imagen)

class Videojuegos(models.Model):
    titulo = models.CharField(max_length=100, null=True)
    casa_desarrolladora = models.CharField(max_length=100, null=True)
    imagen = models.FileField(upload_to='videojuegos/',null=True,verbose_name="")

    def __str__(self):
        return self.titulo + ":" + str(self.imagen)

class Peliculas(models.Model):
    titulo = models.CharField(max_length=100, null=True)
    casa_productora = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    imagen = models.FileField(upload_to='peliculas/',null=True,verbose_name="")
    def __str__(self):
        return self.titulo + ":" + str(self.imagen)

class Series(models.Model):
    titulo = models.CharField(max_length=100, null=True)
    casa_productora = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    imagen = models.FileField(upload_to='series/',null=True,verbose_name="")
    def __str__(self):
        return self.titulo + ":" + str(self.imagen)

# Create your models here.
