from django.contrib import admin, messages
from .models import Unit, Classroom, Lecturer, Student, Faculty, Semester, TimeSlot
from .forms import AssignUnitForm
from django.urls import reverse, path
from django.utils.html import format_html
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from .models import Unit, ClassTimetable
from .views import generate_class_timetable_view  # Import your timetable generation function

# Customize the default admin site
admin.site.site_header = "My School Administration"
admin.site.site_title = "My School Administration"
admin.site.index_title = "Welcome to My School Administration"

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'is_available')  # Include 'is_available' in the list
    list_editable = ('is_available',)  # Allow editing 'is_available' directly in the list view
    search_fields = ('name',)
    list_per_page = 10

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('lecturer_name', 'faculty')  # Use a custom method for "lecturer_name"
    search_fields = ('user__first_name', 'user__last_name', 'faculty__name')
    list_per_page = 10

    # Custom method to display the lecturer name
    def lecturer_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    # Specify the column name
    lecturer_name.short_description = 'LECTURER'

    # Custom view to show related units and semesters
    def get_related_units_and_semesters(self, obj):
        units = obj.assigned_units.all()  # Access the assigned units
        if units:
            return ", ".join(
                [f"{unit.name} (Semester: {unit.semester.name})" for unit in units]
            )
        return "No units assigned"

    get_related_units_and_semesters.short_description = "Units and Semesters"

    readonly_fields = ['get_related_units_and_semesters']

    fieldsets = (
        (None, {
            'fields': ('user', 'faculty', 'get_related_units_and_semesters'),
        }),
    )

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'user_first_name', 'user_last_name', 'faculty', 'enroll_student', 'view_profile')
    search_fields = ('student_id', 'user__first_name', 'user__last_name', 'faculty__name')
    list_per_page = 10

    # Display the student's first name
    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = 'User First Name'

    # Display the student's last name
    def user_last_name(self, obj):
        return obj.user.last_name
    user_last_name.short_description = 'User Last Name'

    # Link for Enroll functionality
    def enroll_student(self, obj):
        url = reverse('enroll_student', args=[obj.id])  # Adjust if the name of the view is different
        return format_html('<a href="{}">Enroll</a>', url)
    enroll_student.short_description = 'Enroll Student'

    # New functionality: View Profile
    def view_profile(self, obj):
        url = reverse('admin_student_profile', args=[obj.id])
        return format_html('<a href="{}">View Profile</a>', url)
    view_profile.short_description = 'View Profile'




    
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_per_page = 10
    list_filter = ('name',) # This helps ordering Faculties according to their names
   
@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    from django.contrib import admin
from .models import Unit

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'faculty', 'lecturer', 'total_hours', 'physical_hours', 'online_hours', 'enrolled_students_count')
    search_fields = ('code', 'name', 'faculty__name', 'lecturer__user__first_name', 'lecturer__user__last_name')
    list_per_page = 10


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'is_available')  # Show availability in admin
    list_editable = ('is_available',)  # Allow toggling availability directly in the list view

    
   

class GenerateTimetableAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('generate_timetable/', self.admin_site.admin_view(self.generate_timetable), name='generate_timetable'),
        ]
        return custom_urls + urls

    def generate_timetable(self, request):
        generate_timetable()  # Call the function
        self.message_user(request, "Timetable generated successfully!")
        return HttpResponseRedirect("../")
    

class ClassTimetableAdmin(admin.ModelAdmin):
    list_display = ['unit', 'day', 'classroom', 'time', 'status', 'duration']
    
    # Add a custom button for generating the timetable
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('generate-timetable/', self.admin_site.admin_view(self.generate_timetable), name='generate_timetable'),
        ]
        return custom_urls + urls

    def generate_timetable(self, request):
        # Call the function to generate the timetable
        generate_class_timetable_view(request)
        messages.success(request, "Class timetable generated successfully!")
        return redirect('..')  # Redirect back to the admin page

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['custom_button'] = True
        return super().changelist_view(request, extra_context)


# Register the model admin
admin.site.register(ClassTimetable, ClassTimetableAdmin)








