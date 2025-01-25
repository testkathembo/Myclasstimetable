from django.contrib import admin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count
from .models import Student, Unit, Semester, StudentUnitEnrollment, Lecturer, TimeSlot, Classroom, ClassTimetable
from users.models import CustomUser  # Assuming `CustomUser` is your user model
from django.db import models
from random import choice
from datetime import time


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


# Generate timetable
def generate_timetable():
    available_slots = TimeSlot.objects.all()

    for unit in Unit.objects.all():
        for slot in available_slots:
            # Check if a classroom with sufficient capacity is available
            if slot.classroom.capacity >= unit.unit_enrollments.count():
                Timetable.objects.create(
                    unit=unit,
                    classroom=slot.classroom,
                    day=slot.day,
                    time_slot=slot
                )
                slot.is_available = False
                slot.save()
                break


def unit_enrollment_view(request):
    # Fetch units and calculate enrolled students for each semester dynamically
    units = Unit.objects.annotate(
        enrolled_students=Count('unit_enrollments'),
        semester_list=models.Subquery(
            StudentUnitEnrollment.objects.filter(unit=models.OuterRef('pk'))
            .values('semester__name')
            .annotate(count=Count('student'))
            .order_by('-count')
            .values('semester__name')[:1]
        )
    ).select_related('faculty', 'lecturer')

    return render(request, 'school/units_enrollment.html', {'units': units})



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
    
def generate_class_timetable(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time_slots = [time(8, 0), time(10, 0), time(13, 0), time(15, 0)]  # Example times
    classrooms = Classroom.objects.all()
    
    # Clear existing timetable
    ClassTimetable.objects.all().delete()

    for unit in Unit.objects.all():
        enrolled_students = StudentUnitEnrollment.objects.filter(unit=unit).count()
        status = 'physical' if unit.physical_hours > 0 else 'online'
        assigned_day = choice(days)
        assigned_time = choice(time_slots)
        assigned_classroom = None

        # Assign classroom if physical
        if status == 'physical':
            for classroom in classrooms:
                if classroom.capacity >= enrolled_students:
                    assigned_classroom = classroom
                    break

        # Create timetable entry
        ClassTimetable.objects.create(
            unit=unit,
            day=assigned_day,
            classroom=assigned_classroom,
            time=assigned_time,
            status=status
        )

    messages.success(request, "Class timetable has been generated.")
    return redirect('class_timetable_view')  # Replace with the appropriate view

def class_timetable_view(request):
    timetable = ClassTimetable.objects.all()
    return render(request, 'school/class_timetable.html', {'timetable': timetable})







