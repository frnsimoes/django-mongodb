from django.http.response import JsonResponse
from django.utils.dateparse import parse_date
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django.db import connection

from core.filters import NumberofFilter, RaCampusFilter, StudentsFilter

from .models import Students
from .serializers import CampusSerializer, StudentsSerializer


class StudentsListView(generics.ListAPIView):

    """

    (endpoint 1)
    View to list all students in the collection

    * Filter by 'data_inicio'; format: yy-mm-dd 
    query parameter
    * Filter by 'data_fim'; format: yy-mm-dd 
    query parameter
    * Filter by 'modalidade' query parameter


    """

    serializer_class = StudentsSerializer
    queryset = Students.objects.all().order_by('-data_inicio')
    filter_backends = [DjangoFilterBackend]
    filter_class = StudentsFilter
    filterset_fields = ['modalidade', 'data_inicio']


class CampusListView(generics.ListAPIView):

    """
    (endpoint 2)

    View to list a Campus and its corresponding
    courses. It's filtred by the document, so
    there is no aggregation of courses by campus.

    * Filter by 'campus' query parameter

    """
    serializer_class = CampusSerializer
    queryset = Students.objects.values('campus', 'curso')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['campus']


class NumberOfStudentsListView(generics.ListAPIView):

    """
    (endpoint 3)

    Important: Don't test through swagger ("/")

    Access the url to test:

    Example:
    * /students/count/?data_inicio=2016-02-02&data_fim=2021-05-12&campus=AQ

    View to list all students in the collection


    Filters:
    * data_inicio; format: yy-mm-dd 
    * data_fim'; format: yy-mm-dd 
    * campus

    Returns the count, or sum, of documents relative to the
    parameters.
    """

    serializer_class = StudentsSerializer
    queryset = Students.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filter_class = NumberofFilter
    # filterset_fields = ['campus', 'data_inicio']

    def get(self, request):
        resp = Students.objects.all()

        data_inicio = self.request.query_params.get('data_inicio')
        data_fim = self.request.query_params.get('data_fim')
        campus = self.request.query_params.get('campus')

        if data_inicio and data_fim and campus:

            resp = resp.filter(data_inicio__gte=data_inicio,
                               data_inicio__lte=data_fim
                               ).filter(campus=campus).count()

        else:

            resp = {
                'error': {
                    'data_inicio parameter': 'yy-mm-dd',
                    'data_fim parameter': 'yy-mm-dd',
                    'campus': [
                        'AQ',
                        'CB',
                        'CG',
                        'CX',
                        'DR',
                        'JD',
                        'NV',
                        'PP',
                        'TL',
                    ]

                }
            }

        return Response({'Number of students': resp})


class CreateStudent(generics.CreateAPIView):
    """
    (endpoint 4)

    View to create a student document. 
    """

    serializer_class = StudentsSerializer
    queryset = Students.objects.all()
    filter_backends = [DjangoFilterBackend]


class SearchStudent(generics.ListAPIView):

    """
    (endpoint 5)

    View to search a student document.

    * Filter by 'ra', this view doesn't
    allow search by substring.
    """

    serializer_class = StudentsSerializer
    queryset = Students.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ra']

    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        print(connection.queries)
        return super().get(*args, **kwargs)


class StudentsDetail(APIView):

    """
    (endpoint 6)
    View to get a certain document. 

    URL values needed:

    * Ra
    * Campus

    /students/{ra}/{campus}

    """

    def get_object(self, request, *args, **kwargs):
        ra = self.kwargs.get('ra')
        campus = self.kwargs.get('campus')
        try:
            resp = get_object_or_404(Students, ra=ra, campus=campus)
        except Students.MultipleObjectsReturned:
            resp = Students.objects.all()

        return resp

    @method_decorator(cache_page(60*60*2))
    def get(self, request, ra, campus):
        student = self.get_object(ra, campus)

        try:
            serializer = StudentsSerializer(student)
            print(connection.queries) # testando cache

            return Response(serializer.data, status=status.HTTP_200_OK)

        except AttributeError:
            response_error = {
                'Error': 'Mutiple objects returned',
            }

            return JsonResponse(response_error)

    def delete(self, request, ra, campus):
        student = self.get_object(ra, campus)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
