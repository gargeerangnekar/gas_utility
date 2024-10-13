import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gas_utility.settings')
django.setup()

from django.contrib.auth.models import User

# Create a default user
def create_default_user():
    username = 'defaultuser'
    email = 'defaultuser@example.com'
    password = 'password123'

    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username=username, email=email, password=password)
        print("Default user created.")
    else:
        print("Default user already exists.")

if __name__ == "__main__":
    create_default_user()
