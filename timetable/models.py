from django.db import models
from users.models import CustomUser
from faculties.models import Faculty


# models for unit,rooms and timetable
class Unit(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'lecturer'})

class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    
class Timetable(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    day = models.CharField(max_length=10) #  Monday, Tuesday...
    time_start = models.TimeField()
    time_end = models.TimeField()
    
    class Meta:
        unique_together = ['room', 'day', 'time_start', 'time_end'] #  Avoid time conflict
        
    
    