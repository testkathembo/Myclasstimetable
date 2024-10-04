from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Timetable, Unit
from django.core.exceptions import PermissionDenied

# Create your views here.

@login_required
def manage_timetable(request):
    if request.user.role != 'admin' or request.user.faculty is None:
        raise PermissionDenied("You are not allowed to manage this timetable.")
    #  Fetch and display timetables for the admin's faculty
    timetables = Timetable.objects.filter(unit__faculty=request.user.faculty)
    return render(request, 'timetable/manage.html', {'timetables': timetables})

@login_required
def delete_timetable(request,pk):
    if request.user.role != 'admin' or request.user.faculty is None:
        raise PermissionDenied("You are not allowed to delete this timetable.")
    
    timetable = Timetable.objects.get(pk=pk)
    if timetable.unit.faculty != request.user.faculty:
        raise PermissionDenied("You cannot delete timetables from other faculties.")
    
    timetable.delete()
    return redirect('manage_timetable')



