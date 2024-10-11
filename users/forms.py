from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email Address',
        help_text='Enter a valid email address'
    )
    phone = forms.CharField(
        max_length=15, 
        label='Phone Number',
        help_text='Enter your unique phone number'
    )
    role = forms.ChoiceField(
        choices=CustomUser.ROLES,  # Reference the ROLES class attribute
        label='Role',
        help_text='Select your role (Admin, Lecturer or Student)'
    )
    faculty = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(role=CustomUser.LECTURER),
        required=False,
        help_text='Select your associated faculty (if applicable).'
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2', 'role', 'faculty']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom placeholders for form fields if needed
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter first name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter last name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter email address'})
        self.fields['phone'].widget.attrs.update({'placeholder': 'Enter phone number'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})
        self.fields['role'].widget.attrs.update({'placeholder': 'Select your role'})
        self.fields['faculty'].widget.attrs.update({'placeholder': 'Select faculty if applicable'})

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        label='Username',
        help_text='Enter your username',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        label='Password',
        help_text='Enter your password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        
User = get_user_model()  # This ensures Django uses your custom user model

class CustomPasswordResetForm(PasswordResetForm):
    username = forms.CharField(max_length=150, required=True, label="Username")

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        # Check if the username and email match for the custom user model
        try:
            user = User.objects.get(username=username, email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("The provided username and email do not match.")
        return cleaned_data

