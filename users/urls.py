from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from users import views as user_views
from school import views as school_views

urlpatterns = [
    # User authentication URLs
    path('register/', user_views.register, name='register'),
    path('login/', user_views.custom_login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html', next_page='login'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', user_views.CustomPasswordResetView.as_view(), name='password_reset_form'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', user_views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # User profile and dashboards
    path('profile/', user_views.profile, name='profile'),
    path('lecturer_dashboard/', user_views.lecturer_dashboard, name='lecturer_dashboard'),
    path('student_dashboard/', user_views.student_dashboard, name='student_dashboard'),

    # School management URLs
    path('units/<int:unit_id>/assign/', school_views.assign_unit_to_lecturer, name='assign_unit_to_lecturer'),
    path('students/<int:student_id>/enroll/', school_views.enroll_student, name='enroll_student'),
    path('students/<int:student_id>/enroll_units/', school_views.enroll_units, name='enroll_units'),
    path('students/<int:student_id>/enrollment_summary/', school_views.enrollment_summary, name='enrollment_summary'),
    path('students/<int:student_id>/profile/', school_views.student_profile, name='student_profile'),
    path('students/', school_views.student_list, name='student_list'),
    path('units-enrollment/', school_views.unit_enrollment_view, name='units_enrollment'),
    path('students/<int:student_id>/delete_unit/<int:unit_id>/', school_views.delete_unit_enrollment, name='delete_unit_enrollment'),
    path('class-timetable/', school_views.class_timetable_view, name='class_timetable_view'),
    path('generate-timetable/', school_views.generate_class_timetable_view, name='generate_class_timetable'),
]
