
# Gas Utility Customer Service Application

## Overview
This Django application provides an interface for customers of a gas utility company to submit service requests, track the status of their requests, and communicate with the support team. Additionally, it provides an admin dashboard for customer support representatives to manage and track customer service requests.

## Prerequisites
Ensure you have Django installed and the project set up. Install the necessary dependencies using:

```bash
pip install -r requirements.txt
```

## Migrations
Run the migrations to create the necessary database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Default Credentials
- **Default User**: 
    - Username: `defaultuser`
    - Password: `password123`
- **Admin User**: 
    - Username: `adminuser`
    - Password: `adminpassword123`

---

## User Journey (Customer)

### 1. **Login**
   Navigate to `/accounts/login/` to log in as a default user.

- **URL**: `http://127.0.0.1:8000/accounts/login/`
- **Credentials**: 
    - Username: `defaultuser`
    - Password: `password123`

### 2. **Submit a Service Request**
   Once logged in, you can navigate to the service request creation page and submit a new request:

- **URL**: `http://127.0.0.1:8000/service/create/`
- **Steps**: Fill out the form specifying the type of request, description, and optional attachment.

### 3. **Track Request Status**
   After submitting a request, you can view the status of your request:

- **URL**: `http://127.0.0.1:8000/service/status/<request_id>/`

### 4. **View Notifications**
   You can view notifications regarding updates to your service requests:

- **URL**: `http://127.0.0.1:8000/service/notifications/`

---

## Admin Journey (Customer Support)

### 1. **Login**
   Navigate to the admin login page to log in as the admin.

- **URL**: `http://127.0.0.1:8000/admin/`
- **Credentials**: 
    - Username: `adminuser`
    - Password: `adminpassword123`

### 2. **Admin Dashboard**
   After logging in, you can access the admin panel to view and manage customer service requests.

- **URL**: `http://127.0.0.1:8000/service/admin/dashboard/`
- **Steps**:
    - View all customer service requests.
    - Update the status of any request.
    - View comments and interact with customers.

### 3. **Manage Users**
   The admin panel allows you to add or modify user accounts, view service requests, and more.

---

## Running the Server
To start the Django development server, use:

```bash
python manage.py runserver
```

You can now access the application on `http://127.0.0.1:8000/` and follow the user or admin journey.

## Conclusion
This application is designed to simplify customer service management for gas utility companies by allowing customers to submit, track, and communicate about service requests, while providing admins with a powerful tool to manage all incoming requests.
