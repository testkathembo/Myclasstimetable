from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomLoginForm, CustomPasswordResetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView


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
    return render(request, 'users/student_dashboard.html')  # Render student dashboard
