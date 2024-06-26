from rest_framework import serializers
from  baowebapp.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["student_id", "name", "gender", "school"]