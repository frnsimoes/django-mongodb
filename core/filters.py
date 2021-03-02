from .models import Students
from django_filters import FilterSet
import django_filters
from .models import CHOICES_CAMPUS


class StudentsFilter(FilterSet):

    data_inicio = django_filters.DateFromToRangeFilter(
        label = 'Data de início e data de fim. Formato dos campos: yy-mm-dd'
    )

    class Meta:
        model = Students
        fields = ['modalidade']
