from .models import Students
from django_filters import FilterSet, IsoDateTimeFilter
import django_filters
from django_filters.widgets import RangeWidget
from .models import CHOICES_CAMPUS


class StudentsFilter(FilterSet):

    data_inicio = django_filters.DateFilter(field_name='data_inicio',
                                            lookup_expr='gte',
                                            )
    data_fim = django_filters.DateFilter(field_name='data_fim',
                                         lookup_expr='lte',
                                         )

    class Meta:
        model = Students
        fields = ['data_inicio', 'data_fim', 'modalidade']


class NumberofFilter(FilterSet):
    
    data_inicio = django_filters.DateFilter(field_name='data_inicio',
                                            lookup_expr='gte')
                                            
                                            
    data_fim = django_filters.DateFilter(field_name='data_fim',
                                         lookup_expr='lte')
                                         
    
    campus = django_filters.ChoiceFilter(field_name='campus', label='Nome do campus', choices=CHOICES_CAMPUS)

    class Meta:
        models = Students
        fields = ['campus', 'data_inicio', 'data_fim']
