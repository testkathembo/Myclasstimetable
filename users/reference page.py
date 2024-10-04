To create a user-friendly registration and login form for your Django project, I'll guide you through setting up both forms using id, code, fname, lname, email, phone, password, and role fields.

We'll enhance the forms using Django's built-in crispy-forms for better styling, and use some frontend basics for the UI. Here's a detailed guide.

Step 1: Install Required Packages
Crispy Forms: Crispy Forms is a great tool to make your forms look elegant without writing much CSS.

Run the following command to install:

pip install django-crispy-forms
Update settings.py: Add crispy_forms to the INSTALLED_APPS and set the template pack:

INSTALLED_APPS = [
    ...
    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
Step 2: Create a Registration Form
1. Custom User Model
Ensure that the custom user model is updated with the required fields (id, code, fname, lname, email, phone, password, and role).

In users/models.py:

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)  # Unique phone number
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('lecturer', 'Lecturer'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.fname} {self.lname}"
2. Create the Registration Form
In users/forms.py, create the registration form using Django's UserCreationForm and include the necessary fields:

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    code = forms.CharField(max_length=20, label='User Code')
    fname = forms.CharField(max_length=50, label='First Name')
    lname = forms.CharField(max_length=50, label='Last Name')
    email = forms.EmailField(label='Email Address')
    phone = forms.CharField(max_length=15, label='Phone Number')
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, label='Role')

    class Meta:
        model = CustomUser
        fields = ['id', 'code', 'fname', 'lname', 'email', 'phone', 'password1', 'password2', 'role']
Step 3: Create Views for Registration and Login
In users/views.py, define views for both the registration and login functionality.

Registration View:

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to home after registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})
Login View: Django has built-in authentication views for login and logout, but you can customize them by creating your own views.

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})
    
Step 4: Create the HTML Templates
In the templates/users/ directory, create the HTML files for the registration and login forms.

1. Registration Template (register.html):

{% extends 'base.html' %}

{% block content %}
<div class="container mt-5">
    <h2>Register</h2>
    <form method="POST">
        {% csrf_token %}
        {{ form|crispy }}
        <button type="submit" class="btn btn-primary mt-3">Register</button>
    </form>
</div>
{% endblock %}

2. Login Template (login.html):

{% extends 'base.html' %}

{% block content %}
<div class="container mt-5">
    <h2>Login</h2>
    <form method="POST">
        {% csrf_token %}
        {{ form|crispy }}
        <button type="submit" class="btn btn-primary mt-3">Login</button>
    </form>
</div>
{% endblock %}

Step 5: URL Configuration
In users/urls.py, add URL patterns for both registration and login views:


from django.urls import path
from .views import register, login_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
]
Then, in your main urls.py, include the users app URL patterns:

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]

Step 6: Styling the Forms
Django Crispy Forms automatically handles the basic form styling. To give it a professional look:

Make sure your project uses Bootstrap.
Include Bootstrap CSS in your base template.
In templates/base.html:

html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MyClass Timetable</title>
    <!-- Include Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

{% block content %}
{% endblock %}

<!-- Include Bootstrap JS (optional) -->
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

Step 7: Migrations and Running the Server
Make migrations for the custom user model and apply them:


python manage.py makemigrations
python manage.py migrate
Run your development server:

bash
Copy code
python manage.py runserver
Step 8: Test the Forms
Visit the following URLs:

Register: http://127.0.0.1:8000/users/register/
Login: http://127.0.0.1:8000/users/login/
You should now have working and well-styled registration and login forms with the fields id, code, fname, lname, email, phone, password, and role.

Conclusion
You've now set up a complete and user-friendly registration and login system in Django, using custom user fields. You can further enhance the look and functionality by adding more form validation, error messages, or custom redirects based on user roles.






You said:
I hope in the user will be able to login based on his role because I want to have only one login form
ChatGPT said:
ChatGPT
Absolutely! You can implement a single login form and direct users to different views based on their role (admin, lecturer, student) after they successfully log in. To achieve this, we can enhance the existing login view logic to check the user's role and redirect them accordingly.

Here’s how you can do it:

Steps to Implement Role-Based Login in Django
Step 1: Update the Custom User Model (if necessary)
Ensure your CustomUser model includes the role field, which you've already defined. Here’s a recap of what it should look like:

python
Copy code
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, unique=True)
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('lecturer', 'Lecturer'),
        ('student', 'Student'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f"{self.fname} {self.lname}"
Step 2: Customize the Login View
In your users/views.py, modify the login_view to redirect users based on their role after successful authentication.

Here’s an example of how you can handle role-based redirection after login:

python
Copy code
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                # Redirect user based on their role
                if user.role == 'admin':
                    return redirect(reverse('admin_dashboard'))
                elif user.role == 'lecturer':
                    return redirect(reverse('lecturer_dashboard'))
                elif user.role == 'student':
                    return redirect(reverse('student_dashboard'))
                else:
                    return redirect('home')  # Fallback if role is not recognized
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})
Step 3: Create Role-Based Views
You need to create separate views for each role, such as an admin dashboard, lecturer dashboard, and student dashboard.

In users/views.py:

python
Copy code
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')

@login_required
def lecturer_dashboard(request):
    return render(request, 'users/lecturer_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'users/student_dashboard.html')
Step 4: Update URLs
In users/urls.py, map each view to a URL. This will ensure that after login, users are redirected to their respective dashboards.

python
Copy code
from django.urls import path
from .views import login_view, admin_dashboard, lecturer_dashboard, student_dashboard

urlpatterns = [
    path('login/', login_view, name='login'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('lecturer_dashboard/', lecturer_dashboard, name='lecturer_dashboard'),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
]
Step 5: Create Templates for Each Role's Dashboard
You’ll need to create HTML files for each role-based dashboard.

Admin Dashboard: templates/users/admin_dashboard.html

html
Copy code
{% extends 'base.html' %}
{% block content %}
<div class="container">
    <h1>Welcome to the Admin Dashboard</h1>
    <p>Manage the platform here.</p>
</div>
{% endblock %}
Lecturer Dashboard: templates/users/lecturer_dashboard.html

html
Copy code
{% extends 'base.html' %}
{% block content %}
<div class="container">
    <h1>Welcome to the Lecturer Dashboard</h1>
    <p>Manage your classes here.</p>
</div>
{% endblock %}
Student Dashboard: templates/users/student_dashboard.html

html
Copy code
{% extends 'base.html' %}
{% block content %}
<div class="container">
    <h1>Welcome to the Student Dashboard</h1>
    <p>View your timetable here.</p>
</div>
{% endblock %}
Step 6: Protect the Dashboard Views
To ensure that users don’t access dashboards they aren’t authorized for, you can create decorators that check the user’s role before allowing them to access a view.

Here’s how you can create a decorator for each role:

In users/decorators.py:

python
Copy code
from django.http import HttpResponseForbidden
from functools import wraps

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You are not authorized to view this page.")
        return _wrapped_view
    return decorator
Now, use this decorator in your views:

In users/views.py:

python
Copy code
from .decorators import role_required

@login_required
@role_required(['admin'])
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')

@login_required
@role_required(['lecturer'])
def lecturer_dashboard(request):
    return render(request, 'users/lecturer_dashboard.html')

@login_required
@role_required(['student'])
def student_dashboard(request):
    return render(request, 'users/student_dashboard.html')
This ensures that only users with the right role can access the corresponding dashboard.

Step 7: Test the Login
Navigate to the login page: http://127.0.0.1:8000/users/login/
Enter user credentials.
Based on the user’s role, they will be redirected to the appropriate dashboard:
Admin: admin_dashboard
Lecturer: lecturer_dashboard
Student: student_dashboard


=========================

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
URL Configuration:
Make sure you have the URL configuration pointing to the registration view:
python
Copy code
# urls.py in the 'users' app
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
]

