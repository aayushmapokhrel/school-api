from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from school.models import School, Student, Teacher
from school.serializers import (
    SchoolSerializer,
    StudentSerializer,
    TeacherSerializer
)


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all().order_by('id')
    serializer_class = SchoolSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name", "address"]
    permission_classes = [IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related("school")
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name", "grade", "school__name"]
    filterset_fields = ["school", "grade", "age"]
    permission_classes = [IsAuthenticated]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.select_related("school")
    serializer_class = TeacherSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name", "subject", "school__name"]
    filterset_fields = ["school", "subject"]
    permission_classes = [IsAuthenticated]
