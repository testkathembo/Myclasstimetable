from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, custom_login_view, profile, lecturer_dashboard, student_dashboard


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', custom_login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('lecturer_dashboard/', lecturer_dashboard, name='lecturer_dashboard'),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
]

    







