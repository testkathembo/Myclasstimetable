from django.db import models
from django.conf import settings  # For ForeignKey relations with the CustomUser model

class Unit(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    lecturer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'lecturer'},  # Ensure only users with role 'lecturer' can be assigned
        related_name='units'
    )

    def __str__(self):
        return f"{self.code} - {self.name}"


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Classroom: {self.name} (Capacity: {self.capacity})"
    
class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'lecturer'},
        related_name='lecturer_profile'
    )
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='lecturers')

    def __str__(self):
        return f"Lecturer: {self.user.first_name} {self.user.last_name}"

class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'},
        related_name='student_profile'
    )
    student_id = models.CharField(max_length=20, unique=True)
    enrolled_units = models.ManyToManyField(Unit, related_name='students')
    faculty = models.ForeignKey(Faculty, null=True, blank=True, on_delete=models.CASCADE, related_name='students')  # Make this field nullable

    def __str__(self):
        return f"Student: {self.user.first_name} {self.user.last_name} (ID: {self.student_id})"

