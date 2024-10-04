# from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# views.
def send_timetable_ready_email(user):
    subject = "Your Class Timetable is Ready"
    message = "Your class timetable for this semester is ready. Please check it on your portal."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)
    
def notify_all_users_timetable_ready():
    users = CustomUser.objects.filter(role_in=['lecturer', 'student'])
    for user in users:
        send_timetable_ready_email(user)
        
    