from djongo import models

CHOICES_MODALIDADE = (
    ('EAD', 'EAD'),
    ('PRES', 'PRESENCIAL')
)

CHOICES_CAMPUS = (
    ('AQ', 'AQ'),
    ('CB', 'CB'),
    ('CG', 'CG'),
    ('CX', 'CX'),
    ('DR', 'DR'),
    ('JD', 'JD'),
    ('NV', 'NV'),
    ('PP', 'PP'),
    ('TL', 'TL'),
)


class Students(models.Model):

    _id = models.ObjectIdField()

    nome = models.CharField(max_length=200,
                            blank=True)

    idade_ate_31_12_2016 = models.CharField(max_length=20,
                                            blank=True)
                                            
    ra = models.CharField(max_length=15,
                          blank=True)
                          
    campus = models.CharField(choices=CHOICES_CAMPUS,
                              max_length=2,
                              blank=True)

    municipio = models.CharField(max_length=100,
                                 blank=True)

    curso = models.TextField()

    modalidade = models.CharField(choices=CHOICES_MODALIDADE,
                                  max_length=50,
                                  blank=True)

    nivel_do_curso = models.CharField(max_length=50,
                                      blank=True)
                                      
    data_inicio = models.DateField()

    data_fim = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome
