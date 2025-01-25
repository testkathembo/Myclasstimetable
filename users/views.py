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


def custom_login_view(request):
    if request.method == 'POST':  # Fixed to 'POST'
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Log in the user
                
                # Debugging output
                print(f"Logged in user: {user.username}, Role: {user.role}")
                
                # Redirect based on user role
                if user.is_superuser:
                    return redirect('/admin/')  # Redirect to admin panel for superusers
                elif user.role.lower() == 'lecturer':
                    return redirect('lecturer_dashboard')  # Redirect to lecturer dashboard
                elif user.role.lower() == 'student':
                    return redirect('student_dashboard')  # Redirect to student dashboard
                else:
                    messages.error(request, 'Unrecognized role.')
                    return redirect('profile')  # Default redirect for unrecognized roles
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = CustomLoginForm()  # Create a blank form for GET requests

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





