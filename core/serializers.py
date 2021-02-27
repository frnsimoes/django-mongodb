from rest_framework import serializers
from .models import Students
from django.utils.dateparse import parse_date

class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = '__all__'

    def validate_date(self, value):
        if isinstance(self.data_inicio, str):
            return parse_date(self.data_inicio)

class CampusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ('campus', 'curso')