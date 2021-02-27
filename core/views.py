from datetime import datetime
from django.db.models.query import QuerySet

from django.utils.dateparse import parse_date
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from core.filters import NumberofFilter, StudentsFilter

from .models import Students
from .serializers import CampusSerializer, StudentsSerializer


# class CountModelMixin(object):
#     @action(detail=False)
#     def count(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         content = {'count': queryset.count()}
#         return Response(content)

class StudentsListView(mixins.ListModelMixin,
                       viewsets.GenericViewSet):


    serializer_class = StudentsSerializer
    queryset = Students.objects.all().order_by('-data_inicio')
    filter_backends = [DjangoFilterBackend]
    filter_class = StudentsFilter
    filterset_fields = ['modalidade', 'data_inicio', 'data_fim']


class CampusListView(mixins.ListModelMixin,
                     viewsets.GenericViewSet):


    serializer_class = CampusSerializer
    queryset = Students.objects.values('campus', 'curso')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['campus']


class NumberOfStudentsListView(mixins.ListModelMixin,
                               viewsets.GenericViewSet,
                               ):

    serializer_class = StudentsSerializer
    queryset = Students.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = NumberofFilter
    filterset_fields = ['campus', 'data_inicio', 'data_fim']
