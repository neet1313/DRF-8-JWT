from rest_framework import serializers
from API import models


# Model Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['name', 'roll', 'city']
