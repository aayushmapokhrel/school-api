from django.contrib import admin
from school.models import School, Student, Teacher


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "address"]
    search_fields = ["id", "name", "address"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "grade", "school"]
    search_fields = ["id", "name", "age", "grade", "school"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "subject", "school"]
    search_fields = ["id", "name", "subject", "school"]
