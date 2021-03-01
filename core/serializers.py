from rest_framework import serializers
from .models import Students
from django.utils.dateparse import parse_date

class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        exclude = ('_id', )


class CampusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ('campus', 'curso')