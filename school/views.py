from django.contrib import admin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count, Q
from .models import Student, Unit, Semester, StudentUnitEnrollment, Lecturer, TimeSlot, Classroom, ClassTimetable
from users.models import CustomUser  # Assuming `CustomUser` is your user model
from django.db import models
from random import choice
from datetime import time, timedelta

# Inline admin to manage the relationship between students, units, and semesters
class StudentUnitEnrollmentInline(admin.TabularInline):
    model = StudentUnitEnrollment
    extra = 1  # Number of blank forms displayed
    fields = ('unit', 'semester')


# Display all units
def unit_list(request):
    units = Unit.objects.select_related('faculty', 'lecturer', 'semester')
    return render(request, 'school/units_list.html', {'units': units})


# Assign a semester and lecturer to a unit
def assign_semester_and_lecturer(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)
    lecturers = CustomUser.objects.filter(role='lecturer')
    semesters = Semester.objects.all()

    if request.method == 'POST':
        semester_id = request.POST.get('semester')
        lecturer_id = request.POST.get('lecturer')

        if semester_id:
            unit.semester = get_object_or_404(Semester, id=semester_id)
        if lecturer_id:
            lecturer = get_object_or_404(CustomUser, id=lecturer_id)
            unit.lecturer = lecturer

        unit.save()
        messages.success(
            request,
            f"Unit '{unit.name}' assigned to {unit.lecturer.user.first_name} {unit.lecturer.user.last_name} for {unit.semester.name}."
        )
        return redirect('unit_list')  # Redirect to the units list page

    return render(request, 'school/assign_semester_lecturer.html', {
        'unit': unit,
        'lecturers': lecturers,
        'semesters': semesters,
    })


# Enroll a student in units
def enroll_units(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    semesters = Semester.objects.all()
    units = Unit.objects.all()

    if request.method == 'POST':
        selected_units = request.POST.getlist('units')
        semester_id = request.POST.get('semester')

        if not semester_id:
            messages.error(request, "Please select a semester.")
            return render(request, 'school/enroll_units.html', {
                'student': student,
                'semesters': semesters,
                'units': units,
            })

        semester = get_object_or_404(Semester, id=semester_id)

        # Enroll the student in the selected units for the chosen semester
        for unit_id in selected_units:
            unit = get_object_or_404(Unit, id=unit_id)
            StudentUnitEnrollment.objects.get_or_create(
                student=student, unit=unit, semester=semester
            )

        messages.success(request, f"{student.user.first_name} has been successfully enrolled in the selected units.")
        return redirect('enrollment_summary', student_id=student.id)

    return render(request, 'school/enroll_units.html', {
        'student': student,
        'semesters': semesters,
        'units': units,
    })
    
def unit_enrollment_view(request):
    # Annotate units with the count of enrolled students
    units = Unit.objects.annotate(
        enrolled_students=Count('unit_enrollments')
    ).select_related('faculty', 'lecturer')

    # Pass data to the template
    return render(request, 'school/units_enrollment.html', {'units': units})


# Enrollment summary
def enrollment_summary(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    enrolled_units = StudentUnitEnrollment.objects.filter(student=student).select_related('unit', 'semester')

    if request.user.is_superuser:
        messages.success(request, f"{student.user.first_name} has been successfully enrolled in the selected units.")
        return redirect('/admin/school/student/')

    return render(request, 'users/enrollment_summary.html', {
        'student': student,
        'enrolled_units': enrolled_units,
    })


# Assign a unit to a lecturer
def assign_unit_to_lecturer(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)
    lecturers = CustomUser.objects.filter(role='lecturer')
    semesters = Semester.objects.all()

    if request.method == 'POST':
        semester_id = request.POST.get('semester')
        lecturer_id = request.POST.get('lecturer')

        semester = get_object_or_404(Semester, id=semester_id)
        lecturer = get_object_or_404(CustomUser, id=lecturer_id)

        unit.semester = semester
        unit.lecturer = lecturer
        unit.save()

        return redirect('unit_list')

    return render(request, 'school/assign_unit.html', {
        'unit': unit,
        'lecturers': lecturers,
        'semesters': semesters,
    })


def find_available_timeslot(day, start_time, end_time, lecturer, mode, classrooms, unit):
    """
    Helper function to find the first available timeslot for the given constraints.
    """
    current_time = start_time

    while current_time < end_time:
        # Ensure lecturer is available at this time
        lecturer_busy = ClassTimetable.objects.filter(
            day=day,
            time=current_time,
            unit__lecturer=lecturer
        ).exists()
        if lecturer_busy:
            current_time = (datetime.combine(date.today(), current_time) + timedelta(hours=1)).time()
            continue

        # Handle physical and online separately
        if mode == 'physical':
            # Check for an available classroom
            for classroom in classrooms:
                classroom_busy = ClassTimetable.objects.filter(
                    day=day,
                    time=current_time,
                    classroom=classroom
                ).exists()
                if not classroom_busy and classroom.capacity >= unit.enrolled_students_count():
                    return classroom, current_time
        else:
            # For online, no need to check classrooms
            return None, current_time

        # Increment the time
        current_time = (datetime.combine(date.today(), current_time) + timedelta(hours=1)).time()

    return None



# List students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'school/student_list.html', {'students': students})

def enroll_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    units = Unit.objects.all()
    semesters = Semester.objects.all()

    if request.method == "POST":
        selected_units = request.POST.getlist("units")  # Get the selected units
        semester_id = request.POST.get("semester")  # Get the selected semester
        if not selected_units or not semester_id:
            messages.error(request, "Please select both units and a semester.")
            return redirect("enroll_student", student_id=student_id)

        semester = Semester.objects.get(id=semester_id)

        # Enroll the student in the selected units
        for unit_id in selected_units:
            unit = Unit.objects.get(id=unit_id)
            StudentUnitEnrollment.objects.get_or_create(student=student, unit=unit, semester=semester)

        messages.success(request, f"{student.user.first_name} has been successfully enrolled.")
        return redirect("student_list")  # Redirect back to the student list

    context = {
        "student": student,
        "units": units,
        "semesters": semesters,
    }
    return render(request, "school/enroll_student.html", context)

def delete_unit_enrollment(request, student_id, unit_id):
    # Get the enrollment record for the student and unit
    enrollment = get_object_or_404(StudentUnitEnrollment, student_id=student_id, unit_id=unit_id)

    if request.method == "POST":
        # Delete the record
        enrollment.delete()
        messages.success(request, "The unit has been successfully removed from the student's account.")
        return redirect('student_profile', student_id=student_id)  # Replace with your profile view name

    # Render a confirmation page
    return render(request, 'school/confirm_delete_unit.html', {
        'enrollment': enrollment,
    })

def student_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    enrolled_units = student.unit_enrollments.all()
    return render(request, 'school/student_profile.html', {
        'student': student,
        'enrolled_units': enrolled_units
    })

def generate_class_timetable_view(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time_slots = [time(8, 0), time(10, 0), time(13, 0), time(15, 0)]
    classrooms = Classroom.objects.filter(is_available=True)

    # Ensure there's a placeholder classroom for Zoom
    zoom_classroom, created = Classroom.objects.get_or_create(
        name="Zoom",
        defaults={'capacity': 0, 'is_available': False}
    )

    # Clear existing timetable
    ClassTimetable.objects.all().delete()

    # Track added combinations of (unit code, status)
    added_combinations = set()

    for unit in Unit.objects.all():
        physical_hours = unit.physical_hours
        online_hours = unit.online_hours
        enrolled_students = StudentUnitEnrollment.objects.filter(unit=unit).count()

        assigned_slots = {}
        used_days = set()  # Keep track of days used for this unit

        # Handle physical hours
        for _ in range(physical_hours):
            assigned_time = None
            assigned_classroom = None

            for day in days:
                if day in used_days:
                    continue  # Skip days already used for this unit

                if day not in assigned_slots:
                    assigned_slots[day] = set()

                for slot in time_slots:
                    if slot not in assigned_slots[day]:
                        for classroom in classrooms:
                            if (
                                classroom.capacity >= enrolled_students and
                                not ClassTimetable.objects.filter(
                                    day=day, time=slot, classroom=classroom
                                ).exists() and
                                not ClassTimetable.objects.filter(
                                    day=day, time=slot, unit__lecturer=unit.lecturer
                                ).exists()
                            ):
                                assigned_classroom = classroom
                                assigned_time = slot
                                assigned_slots[day].add(slot)
                                used_days.add(day)
                                break

                    if assigned_time:
                        break

                if assigned_time:
                    break

            if assigned_time and assigned_classroom:
                # Avoid duplicate (unit code + status) combinations
                combination_key = (unit.code, 'physical')
                if combination_key not in added_combinations:
                    ClassTimetable.objects.create(
                        unit=unit,
                        day=day,
                        classroom=assigned_classroom,
                        time=assigned_time,
                        status='physical',
                        duration="2 hours"
                    )
                    added_combinations.add(combination_key)

        # Handle online hours
        for _ in range(online_hours):
            assigned_time = None
            assigned_classroom = zoom_classroom  # Online uses Zoom classroom

            for day in days:
                if day in used_days:
                    continue  # Skip days already used for this unit

                if day not in assigned_slots:
                    assigned_slots[day] = set()

                for slot in time_slots:
                    if slot not in assigned_slots[day]:
                        if not ClassTimetable.objects.filter(
                            day=day, time=slot, unit__lecturer=unit.lecturer
                        ).exists():
                            assigned_time = slot
                            assigned_slots[day].add(slot)
                            used_days.add(day)
                            break

                    if assigned_time:
                        break

                if assigned_time:
                    break

            if assigned_time:
                # Avoid duplicate (unit code + status) combinations
                combination_key = (unit.code, 'online')
                if combination_key not in added_combinations:
                    ClassTimetable.objects.create(
                        unit=unit,
                        day=day,
                        classroom=assigned_classroom,
                        time=assigned_time,
                        status='online',
                        duration="2 hours" if online_hours == 2 else "1 hour"
                    )
                    added_combinations.add(combination_key)

    messages.success(request, "Class timetable generated successfully.")
    return redirect('class_timetable_view')



def class_timetable_view(request):
    timetable = ClassTimetable.objects.select_related('unit', 'classroom').all()
    return render(request, 'school/class_timetable.html', {'timetable': timetable})


def generate_timetable_view(request):
    generate_class_timetable()
    messages.success(request, "Class timetable has been successfully generated.")
    return redirect('class_timetable_view')  # Replace with your timetable display view







