from django import forms
from users.models import CustomUser  # Replace with the path to your CustomUser model
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Unit, Semester, StudentUnitEnrollment


class AssignUnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['code', 'name', 'description', 'faculty', 'lecturer']  # Removed 'semester'

        

def enroll_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    units = Unit.objects.all()
    semesters = Semester.objects.all()

    if request.method == 'POST':
        unit_id = request.POST.get('unit')
        semester_id = request.POST.get('semester')

        if unit_id and semester_id:
            unit = Unit.objects.get(id=unit_id)
            semester = Semester.objects.get(id=semester_id)
            StudentUnitEnrollment.objects.create(student=student, unit=unit, semester=semester)
            return redirect('student_list')  # Replace with the correct URL name for the student list

    return render(request, 'school/enroll_student.html', {
        'student': student,
        'units': units,
        'semesters': semesters,
    })

