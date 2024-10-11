from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import (CustomPasswordResetView,register, custom_login_view, CustomPasswordResetCompleteView, profile, lecturer_dashboard, student_dashboard,
)


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', custom_login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html', next_page='login'), name='logout'),  # Use custom logout template 
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset_form'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Use custom view here
    path('profile/', profile, name='profile'),
    path('lecturer_dashboard/', lecturer_dashboard, name='lecturer_dashboard'),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
]