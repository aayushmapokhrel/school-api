from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def str(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def str(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def str(self):
        return self.name
