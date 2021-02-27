from django_filters.filters import CharFilter, ChoiceFilter
from .models import Students
from django_filters import FilterSet, IsoDateTimeFilter
from .models import CHOICES_CAMPUS

class EventFilter(FilterSet):
    class Meta:
        model = Students
        fields = {
            'data_inicio': ('lte', ),
            'data_fim': ('gte', ),
            'campus': ('icontains', ),
            
        }

    filter_overrides = {
        Students.data_inicio: {
            'filter_class': IsoDateTimeFilter
        },
        Students.data_fim: {
            'filter_class': IsoDateTimeFilter
        },
        Students.campus: {
            'filter_class': ChoiceFilter(choices=CHOICES_CAMPUS)
        },
    }

# class CampusFilter(FilterSet):
#     class Meta: 
#         model = Students
#         fields = ['campus']
#         filter_overrides = {
#             Students.campus: {
                
#             }
#         }