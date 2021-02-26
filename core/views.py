from rest_framework.views import APIView
from rest_framework import viewsets, mixins
from .models import Students
from datetime import datetime
from .serializers import StudentsSerializer
from rest_framework.response import Response


class StudentsListView(mixins.ListModelMixin,
                       viewsets.GenericViewSet):

    serializer_class = StudentsSerializer
    ordering = ['-data_inicio']


    def get_queryset(self):
        queryset = ''

        modalidade_param = self.request.query_params.get('modalidade_param')
        if modalidade_param:
            queryset = Students.objects.filter(
                modalidade=modalidade_param).order_by('-data_inicio')

        data_inicio_param = self.request.query_params.get('data_de_inicio_param')
        if data_inicio_param:
            data_inicio_param = datetime.fromisoformat(data_inicio_param)
            queryset = Students.objects.all()

        return queryset
