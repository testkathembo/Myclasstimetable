from django.contrib import admin
from .models import Unit, Classroom, Lecturer, Student, Faculty

# Customize the default admin site
admin.site.site_header = "My School Administration"
admin.site.site_title = "My School Administration"
admin.site.index_title = "Welcome to My School Administration"

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'lecturer')
    search_fields = ('code', 'name')
    list_filter = ('lecturer',)
    list_per_page = 10


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')
    search_fields = ('name',)
    list_filter = ('capacity',)
    list_per_page = 10


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('user', 'faculty')
    search_fields = ('user__first_name', 'user__last_name', 'faculty')
    list_per_page = 10

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
    list_per_page = 10
    
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_per_page = 10
    list_filter = ('name',) # This helps ordering Faculties according to their names
