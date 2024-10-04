from django.db import models
from users.models import CustomUser

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='faculty_admin')

    def __str__(self):
        return self.name

    
