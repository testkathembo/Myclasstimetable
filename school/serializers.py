from rest_framework import serializers
from .models import ClassTimetable, Unit, Classroom


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['name', 'code']  # Include only relevant fields


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name', 'capacity']  # Include only relevant fields


from rest_framework import serializers
from .models import ClassTimetable

class ClassTimetableSerializer(serializers.ModelSerializer):
    unit_name = serializers.CharField(source='unit.name', read_only=True)
    unit_code = serializers.CharField(source='unit.code', read_only=True)
    lecturer_name = serializers.SerializerMethodField()
    classroom_name = serializers.CharField(source='classroom.name', read_only=True)

    class Meta:
        model = ClassTimetable
        fields = ['id', 'unit_name', 'unit_code', 'day', 'classroom_name', 'time', 'status', 'lecturer_name', 'duration']

    def get_lecturer_name(self, obj):
        if obj.unit and obj.unit.lecturer:
            return f"{obj.unit.lecturer.user.first_name} {obj.unit.lecturer.user.last_name}"
        return "N/A"

    
    