from django.contrib import admin
from .models import Unit, Classroom, Lecturer, Student

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'lecturer')
    search_fields = ('code', 'name')
    list_filter = ('lecturer',)


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')
    search_fields = ('name',)
    list_filter = ('capacity',)


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('user', 'faculty')
    search_fields = ('user__first_name', 'user__last_name', 'faculty')

    # Ensure that permissions are correctly set
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # Allow superuser to change

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # Allow superuser to delete


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id')
    search_fields = ('user__first_name', 'user__last_name', 'student_id')
    filter_horizontal = ('enrolled_units',)  # For selecting multiple units

