from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, first_name='', last_name='', phone='', **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        
        email = self.normalize_email(email)  # Normalize the email
        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)  # Hash the password
        user.save(using=self._db)  # Save the user to the database
        return user
    
    def create_superuser(self, username, email, password=None, first_name='', last_name='', phone='', **extra_fields):
        """Create and return a superuser with the given details."""
        # Ensure required fields are set for superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        return self.create_user(username, email, password, first_name=first_name, last_name=last_name, phone=phone, **extra_fields)
    
    def get_by_natural_key(self, username):
        """Retrieve a user by their natural key (username)."""
        return self.get(username=username)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ADMIN = 'admin'
    LECTURER = 'lecturer'
    STUDENT = 'student'

    ROLES = [
        (ADMIN, 'Admin'),
        (LECTURER, 'Lecturer'),
        (STUDENT, 'Student'),
    ]

    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, blank=True)  # Made optional
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=10, choices=ROLES)  # Define choices here
    faculty_id = models.BigIntegerField(null=True, blank=True)  # Made optional

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = CustomUserManager()  # Set custom manager here

    def __str__(self):
        return self.username
