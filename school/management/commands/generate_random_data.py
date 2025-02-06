import random
from django.core.management.base import BaseCommand
from faker import Faker
from school.models import Student, Faculty, Semester, Unit
from users.models import CustomUser  # Assuming CustomUser is your user model


class Command(BaseCommand):
    help = 'Generate random data for the database'

    def add_arguments(self, parser):
        # Optional arguments to customize data generation
        parser.add_argument('--students', type=int, help='Number of students to create', default=10)
        parser.add_argument('--faculties', type=int, help='Number of faculties to create', default=5)
        parser.add_argument('--semesters', type=int, help='Number of semesters to create', default=3)
        parser.add_argument('--units', type=int, help='Number of units to create', default=10)

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create faculties
        num_faculties = kwargs['faculties']
        faculties = []
        for _ in range(num_faculties):
            faculty = Faculty.objects.create(
                name=fake.unique.company(),
                description=fake.text()
            )
            faculties.append(faculty)
        self.stdout.write(f"Created {num_faculties} faculties.")

        # Create semesters
        num_semesters = kwargs['semesters']
        semesters = []
        for i in range(1, num_semesters + 1):
            semester = Semester.objects.create(name=f"Semester {i}")
            semesters.append(semester)
        self.stdout.write(f"Created {num_semesters} semesters.")

        # Create students
        num_students = kwargs['students']
        for _ in range(num_students):
            user = CustomUser.objects.create_user(
                username=fake.unique.user_name(),
                email=fake.unique.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                role='student',  # Assuming your user model has a `role` field
                password='password123'  # Set a default password
            )
            student = Student.objects.create(
                user=user,
                student_id=fake.unique.random_int(min=10000, max=99999),
                faculty=random.choice(faculties)
            )
        self.stdout.write(f"Created {num_students} students.")

        # Create units
        num_units = kwargs['units']
        for _ in range(num_units):
            unit = Unit.objects.create(
                code=fake.unique.bothify(text='??###'),
                name=fake.unique.job(),
                description=fake.text(),
                faculty=random.choice(faculties),
                total_hours=random.choice([2, 3, 4]),
            )
        self.stdout.write(f"Created {num_units} units.")

        self.stdout.write(self.style.SUCCESS('Random data generation complete!'))
