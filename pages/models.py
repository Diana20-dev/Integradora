from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(verbose_name="Nombre del empleo", max_length=200)
    content = RichTextField(verbose_name="Descripción del empleo")
    order = models.SmallIntegerField(verbose_name="Orden de publicación", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Empleo"
        verbose_name_plural = "Empleos"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class Curriculum(models.Model):
    curriculum = models.FileField(upload_to="curriculums", null=True)