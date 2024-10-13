# service/populate_db.py
import os
import django
from django.contrib.auth.models import User
from service.models import Account, ServiceRequest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gas_utility.settings')
django.setup()

def populate():
    user = User.objects.create_user(username='testuser', password='password')
    account = Account.objects.create(user=user, account_number='123456', address='123 Main St', phone_number='555-1234')

    ServiceRequest.objects.create(user=user, request_type='gas_leak', description='Gas leak in kitchen')
    ServiceRequest.objects.create(user=user, request_type='maintenance', description='Routine check-up')

if __name__ == '__main__':
    populate()
