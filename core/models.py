from django.db.models.fields import CharField
from djongo import models

# Create your models here.

class Students(models.Model):
    _id = models.ObjectIdField()
    nome = models.CharField(max_length=200, blank=True)
    idade_ate_31_12_2016 = models.CharField(max_length=20, blank=True)
    ra = models.CharField(max_length=15, blank=True)
    campus = models.CharField(max_length=2, blank=True)
    municipio = models.CharField(max_length=100, blank=True)
    curso = models.TextField()
    modalidade = models.CharField(max_length=50, blank=True)
    nivel_do_curso = models.CharField(max_length=50, blank=True)
    data_inicio = models.DateField()

    def __str__(self):
        return self.nome