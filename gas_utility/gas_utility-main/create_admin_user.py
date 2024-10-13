
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gas_utility.settings')
django.setup()

from django.contrib.auth.models import User

# Create an admin user
def create_admin_user():
    username = 'adminuser'
    email = 'admin@example.com'
    password = 'adminpassword123'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Admin user created.")
    else:
        print("Admin user already exists.")

if __name__ == "__main__":
    create_admin_user()
