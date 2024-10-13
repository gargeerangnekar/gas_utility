
# Gas Utility Customer Service Django Application Documentation

## Overview
This Django application is designed to streamline customer service requests for a gas utility company. The application allows customers to submit service requests, track the status of their requests, and view account information. Additionally, it provides tools for customer support representatives to manage and process these requests.

## Features

### 1. **Customer Service Request**
- Customers can log in and submit a new service request by specifying:
  - The type of service request (e.g., Gas Leak, Maintenance, Installation).
  - A description of the problem.
  - Attach files if necessary (e.g., images).
- Each request will have a status: **Pending** or **Resolved**.

### 2. **Request Status Tracking**
- Customers can track the status of their service requests, including:
  - The date and time the request was submitted.
  - The current status of the request.
  - The date and time the request was resolved (if applicable).

### 3. **Notifications**
- Customers are notified when the status of their service request changes (e.g., from **Pending** to **Resolved**).

### 4. **Admin Dashboard for Customer Support**
- Support representatives can access an admin dashboard to:
  - View all customer service requests.
  - Filter requests by status or search based on user or request type.
  - Update the status of any request.
  - Add comments to specific service requests for better communication.

### 5. **Comments on Service Requests**
- Both customers and support representatives can add comments to a service request.
- This allows for seamless communication regarding the issue at hand.

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd gas_utility
    ```

2. **Install dependencies:**
    Make sure you have Python and Django installed. You can install the required dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run Migrations:**
    To set up the database, run the following command:
    ```bash
    python manage.py migrate
    ```

4. **Create a superuser for admin access:**
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the application:**
    Start the development server with:
    ```bash
    python manage.py runserver
    ```

6. **Access the application:**
   - **Customer View**: Navigate to `http://localhost:8000/service/create/` to submit a service request.
   - **Admin View**: Access the admin panel at `http://localhost:8000/admin/` to manage service requests and users.

## Project Structure

```
gas_utility/
    manage.py               # Main Django entry point
    gas_utility/
        settings.py         # Project settings
        urls.py             # URL routing configuration
    service/
        models.py           # Database models for service requests, accounts, etc.
        views.py            # Application views handling the request-response cycle
        forms.py            # Forms for creating and editing service requests
        urls.py             # App-specific URLs
        templates/
            service/        # HTML templates for rendering views
        static/             # Static files (CSS, JS, etc.)
        migrations/         # Database migrations
```

## Models

### `auth_user` (Django Default)
- Used to handle users (both customers and admins).

### `service_account`
- Stores account information for each customer (e.g., account number, address, phone number).

### `service_servicerequest`
- Represents customer service requests. Contains fields such as request type, description, status, and attachments.

### `service_notification`
- Stores notifications for customers regarding the status of their service requests.

### `service_comment`
- Allows both customers and support representatives to add comments to a service request for better communication.

## Usage

### Customer Flow:
1. Customer logs in.
2. Submits a service request.
3. Tracks the status of their service request in real time.
4. Receives notifications when the status changes.
5. Can communicate with the support team via comments on the request.

### Support Flow:
1. Support representative logs in via the admin dashboard.
2. Views and manages all service requests.
3. Updates the status of requests and adds comments for communication with customers.
4. Can search and filter requests based on status or type.

## Future Scope and Recommendations

### 1. **Export Service Requests to CSV**
- **Description**: Admins should be able to export all service requests to a CSV file for reporting and data analysis purposes.

### 2. **Service Request Comments**
- **Description**: Allow better communication between customers and support teams by adding comment functionality directly within the service requests.

These additional features would provide better reporting tools and improve customer support interaction within the system.
