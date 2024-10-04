# accounts/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # Ensure the user is logged in to access the profile
def profile(request):
    return render(request, 'users/profile.html')  # Render the user's profile page

@login_required
def lecturer_dashboard(request):
    return render(request, 'users/lecturer_dashboard.html')  # Create this template

@login_required
def student_dashboard(request):
    return render(request, 'users/student_dashboard.html')  # Create this template