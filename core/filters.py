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


class NumberofFilter(FilterSet):

    data_inicio = django_filters.DateFromToRangeFilter(
        label = 'Data de início e data de fim. Formato dos campos: yy-mm-dd'
    )

    campus = django_filters.ChoiceFilter(
        field_name='campus', label='Nome do campus', choices=CHOICES_CAMPUS)

    class Meta:
        models = Students
        fields = ['campus']


class RaCampusFilter(FilterSet):

    ra = django_filters.CharFilter(field_name='ra', lookup_expr='icontains')
    campus = django_filters.CharFilter(
        field_name='campus', lookup_expr='icontains')

    class Meta:

        models = Students
        fields = ['ra']
