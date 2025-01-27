from django.db import models
from django.conf import settings  # For ForeignKey relations with the CustomUser model


class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=255, unique=True)

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
        return f"{self.user.first_name} {self.user.last_name}"


class Unit(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='units')
    lecturer = models.ForeignKey(
        Lecturer, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_units'
    )  # Retaining the 'lecturer' field
    total_hours = models.IntegerField(default=0)
    physical_hours = models.IntegerField(default=0)
    online_hours = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Automatically calculate physical and online hours based on total hours
        if self.total_hours == 4:
            self.physical_hours = 2
            self.online_hours = 2
        elif self.total_hours == 3:
            self.physical_hours = 2
            self.online_hours = 1
        elif self.total_hours == 2:
            self.physical_hours = 2
            self.online_hours = 0
        else:
            self.physical_hours = self.total_hours  # Default to all physical if no specific rule
            self.online_hours = 0

        super().save(*args, **kwargs)

    def enrolled_students_count(self):
        """Count the number of students enrolled in this unit."""
        return self.unit_enrollments.count()

    def __str__(self):
        return f"{self.code} - {self.name}"


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'},
        related_name='student_profile'
    )
    student_id = models.CharField(max_length=20, unique=True)
    faculty = models.ForeignKey(Faculty, null=True, blank=True, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"Student: {self.user.first_name} {self.user.last_name} (ID: {self.student_id})"


class StudentUnitEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='unit_enrollments')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='unit_enrollments')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='unit_enrollments')

    class Meta:
        unique_together = ('student', 'unit', 'semester')

    def __str__(self):
        return f"{self.student.user.first_name} enrolled in {self.unit.name} ({self.semester.name})"
    


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} (Capacity: {self.capacity})"


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"


class ClassTimetable(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='timetable_entries')
    day = models.CharField(max_length=10)  # e.g., Monday, Tuesday
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True, related_name='timetables')  # Allows NULL
    time = models.TimeField(default="08:00:00")
    status = models.CharField(max_length=10, choices=[('online', 'Online'), ('physical', 'Physical')])
    duration = models.CharField(max_length=100, default="2 hour")

    def __str__(self):
        return f"{self.unit.name} on {self.day} at {self.time} ({self.status})"



