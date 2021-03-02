from rest_framework import serializers
from .models import Students

class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        exclude = ('_id', )


class CampusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ('campus', 'curso')