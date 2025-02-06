
from django.urls import path
from . import views

urlpatterns = [
    # Other patterns...
    path('students/<int:student_id>/enroll/', views.enroll_student, name='enroll_student'),
    path('students/<int:student_id>/profile/', views.student_profile, name='admin_student_profile'),
    path('students/', views.student_list, name='student_list'),  # Add this line if not already present    
]


