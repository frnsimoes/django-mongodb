from core.filters import EventFilter
from datetime import datetime
from django.utils.dateparse import parse_date
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
# from .filters import EventFilter

from .models import Students
from .serializers import CampusSerializer, StudentsSerializer


class StudentsListView(mixins.ListModelMixin,
                       viewsets.GenericViewSet):

    """

    1) List all documents, if no parameters

    Parameters

    2) 'Modalidade' param: list documents that matches 'modalidade' ('EAD' or 'PRESENCIAL') param ordered by date.
    3) 'data_inicio' param: list documents oredered by '-data_inicio'

    """

    filter_backends = [DjangoFilterBackend]
    filter_class = EventFilter
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

    def get(self, request):
        """
        Calling 'get' method is not needed, 
        I called because I like to see what's happening.
        """

        students = self.queryset
        serializer = self.serializer_class(students, many=True)
        return Response(serializer.data)


# class CampusListView(mixins.ListModelMixin,
#                      viewsets.GenericViewSet):

    """
    Accepts GET requests:

    1) Lists all documents 

    Parameters

    2) 'Campus' param: list campus with respect course. 

    """

#     serializer_class = CampusSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['campus']

#     def get_queryset(self):
#         queryset = Students.objects.all()

#         campus = self.request.query_params.get('campus')
#         if campus:
#             queryset = queryset.filter(campus__icontains=campus)

#         return queryset


# class NumberOfStudentsListView(mixins.ListModelMixin,
#                                viewsets.GenericViewSet):

#     serializer_class = StudentsSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['campus', 'data_inicio']
#     filter_class = EventFilter
#     queryset = Students.objects.all()
