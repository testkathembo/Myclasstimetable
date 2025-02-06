from django.contrib import admin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count, Q
from django.db import models
from datetime import time, timedelta, datetime
from random import choice
from .models import Student, Unit, Semester, StudentUnitEnrollment, Lecturer, TimeSlot, Classroom, ClassTimetable
from users.models import CustomUser  # Assuming `CustomUser` is your user model



def unit_list(request):
    units = Unit.objects.select_related('faculty', 'lecturer', 'semester')
    return render(request, 'school/units_list.html', {'units': units})


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


def generate_class_timetable_view(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time_slots = [time(8, 0), time(10, 0), time(13, 0), time(15, 0)]
    classrooms = Classroom.objects.filter(is_available=True)

    zoom_classroom, created = Classroom.objects.get_or_create(
        name="Zoom", defaults={'capacity': 0, 'is_available': False}
    )

    ClassTimetable.objects.all().delete()
    added_combinations = set()

    for unit in Unit.objects.all():
        physical_hours = unit.physical_hours
        online_hours = unit.online_hours
        enrolled_students = StudentUnitEnrollment.objects.filter(unit=unit).count()

        assigned_slots = {}
        used_days = set()

        for _ in range(physical_hours):
            assigned_time = None
            assigned_classroom = None

            for day in days:
                if day in used_days:
                    continue

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

        for _ in range(online_hours):
            assigned_time = None
            assigned_classroom = zoom_classroom

            for day in days:
                if day in used_days:
                    continue

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

        messages.success(request, f"Unit '{unit.name}' successfully assigned.")
        return redirect('unit_list')

    return render(request, 'school/assign_unit.html', {
        'unit': unit,
        'lecturers': lecturers,
        'semesters': semesters,
    })

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


def student_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    enrolled_units = StudentUnitEnrollment.objects.filter(student=student).select_related('unit', 'semester')

    return render(request, 'school/student_profile.html', {
        'student': student,
        'enrolled_units': enrolled_units
    })


def student_list(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, 'school/student_list.html', {
        'students': students
    })
    

def unit_enrollment_view(request):
    # Annotate each unit with the number of enrolled students
    units = Unit.objects.annotate(enrolled_students=Count('unit_enrollments'))
    return render(request, 'school/unit_enrollment.html', {'units': units})


def delete_unit_enrollment(request, student_id, unit_id):
    # Retrieve the enrollment record for the given student and unit
    enrollment = get_object_or_404(StudentUnitEnrollment, student_id=student_id, unit_id=unit_id)

    if request.method == "POST":
        # Delete the enrollment record
        enrollment.delete()
        messages.success(request, "Unit has been successfully removed from the student's enrollment.")
        return redirect('student_profile', student_id=student_id)

    # Render a confirmation page before deletion
    return render(request, 'school/confirm_delete_unit.html', {
        'enrollment': enrollment,
    })

