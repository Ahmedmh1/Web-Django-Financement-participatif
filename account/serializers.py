from rest_framework import serializers  # type: ignore
from .models import Project
import psycopg2

class ProjectSerializer(serializers.ModelSerializer):
    class Meta: #class Meta is used to define the fields that we want to expose to the API
        model = Project
        fields = '__all__'
        
