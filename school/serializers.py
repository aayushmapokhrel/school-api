from rest_framework import serializers
from school.models import School, Student, Teacher


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate_age(self, value):
        if value < 5 or value > 20:
            raise serializers.ValidationError("Age must be between 5 and 20")
        return value

    def validate_grade(self, value):
        if not value.strip():
            raise serializers.ValidationError("Grade cannot be empty")
        return value


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

    def validate_subject(self, value):
        if not value.strip():
            raise serializers.ValidationError("Subject cannot be empty")
        return value
