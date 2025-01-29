from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomLoginForm, CustomPasswordResetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView
from django.views.generic import ListView
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from school.models import Student, StudentUnitEnrollment
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse

# Registration view
def register(request):
    if request.method == 'POST':  # Fixed to 'POST'
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('login')  # Redirect to login after successful registration
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()  # Create a blank form for GET requests

    return render(request, 'users/register.html', {'form': form})



@csrf_protect
def custom_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                
                # Redirect to React dashboard based on user role
                if user.is_superuser:
                    return redirect('/admin/')
                elif user.role.lower() == 'lecturer':
                    return redirect('/dashboard/lecturer')
                elif user.role.lower() == 'student':
                    return redirect('/dashboard/student')
                else:
                    return redirect('/dashboard/profile')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomLoginForm()

    return render(request, 'users/login.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    success_url = '/users/password_reset_done'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return redirect('login')


@login_required
def profile(request):
    user = request.user  # Get the logged-in user
    return render(request, 'users/profile.html', {'user': user})  # Pass user data to template


@login_required
def lecturer_dashboard(request):
    return render(request, 'users/lecturer_dashboard.html')  # Render lecturer dashboard


@login_required
def student_dashboard(request):
    # Check if the logged-in user is an admin
    if request.user.is_superuser:
        messages.error(request, "Access Denied: Admins cannot access the student dashboard.")
        return redirect('/admin/school/student/')  # Redirect to the admin student list page
    
    # Fetch the logged-in student
    try:
        student = request.user.student_profile  # Adjust if your model uses another related_name
    except Student.DoesNotExist:
        messages.error(request, "Access Denied: Only students can access this page.")
        return redirect('profile')  # Redirect to a safer page

    # Fetch enrolled units for the student
    enrolled_units = student.unit_enrollments.all()

    return render(request, 'users/student_dashboard.html', {
        'student': student,
        'enrolled_units': enrolled_units,
    })


@login_required
def admin_student_profile(request, student_id):
    # Only superusers can view the profile
    if not request.user.is_superuser:
        messages.error(request, "Access Denied: Only admins can view student profiles.")
        return redirect('/admin/')

    student = get_object_or_404(Student, id=student_id)
    enrolled_units = student.unit_enrollments.all()

    return render(request, 'users/admin_student_profile.html', {
        'student': student,
        'enrolled_units': enrolled_units,
    })
    
    # Restrict user access
    

def is_admin(user):
    return user.role == 'ADMIN'

def is_lecturer(user):
    return user.role == 'LECTURER'

def is_student(user):
    return user.role == 'STUDENT'

@user_passes_test(is_admin)
def admin_dashboard(request):
    # Admin-specific logic here
    return render(request, 'admin_dashboard.html')

@user_passes_test(is_lecturer)
def lecturer_dashboard(request):
    # Lecturer-specific logic here
    return render(request, 'lecturer_dashboard.html')

@user_passes_test(is_student)
def student_dashboard(request):
    # Student-specific logic here
    return render(request, 'student_dashboard.html')


# Redirect user based on role
def custom_login_redirect(request):
    user = request.user
    if user.role == 'ADMIN':
        return redirect('admin_dashboard')
    elif user.role == 'Lecturer':
        return redirect('lecturer_dashboard')
    elif user.role == 'STUDENT':
        return redirect('student_dashboard')
    return redirect('home')



@login_required
def current_user_view(request):
    user = request.user
    data = {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role": getattr(user, "role", "N/A"),  # Assuming role is a custom field
    }
    return JsonResponse(data)







