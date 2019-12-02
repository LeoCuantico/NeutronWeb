from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100 , verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen" , upload_to='projects')
    created = models.DateTimeField(auto_now_add=True , verbose_name="Creación")
    updated = models.DateTimeField(auto_now=True , verbose_name="Actualización")

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created'] ## ordenar segun 'created' de mas nuevo al mas antiguo, anteponer un '-' = '-created' es alrevez

    def __str__(self):
        return self.title