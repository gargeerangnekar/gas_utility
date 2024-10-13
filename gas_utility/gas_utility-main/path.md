# Application Paths

## 1. **Home Page**
- **URL**: `/`
- **Purpose**: Redirects to the login page if the user is not authenticated, otherwise redirects to the dashboard.

## 2. **Login Page**
- **URL**: `/accounts/login/`
- **Purpose**: Allows users to log in to the application.

## 3. **Logout Page**
- **URL**: `/accounts/logout/`
- **Purpose**: Logs the user out of the application.

## 4. **Create Service Request**
- **URL**: `/service/create/`
- **Purpose**: Allows customers to submit a new service request by providing the request type, description, and optional attachment.

## 5. **View Service Request Status**
- **URL**: `/service/status/<int:request_id>/`
- **Purpose**: Displays the status of a service request and allows users to view and add comments related to the request.

## 6. **View Notifications**
- **URL**: `/service/notifications/`
- **Purpose**: Displays all unread notifications related to the user's service requests.

## 7. **Admin Dashboard**
- **URL**: `/service/admin/dashboard/`
- **Purpose**: Provides a dashboard for administrators to view and manage all service requests from customers, with filtering and status update functionality.

## 8. **Django Admin Interface**
- **URL**: `/admin/`
- **Purpose**: Provides an admin interface to manage the application, including users, accounts, service requests, notifications, and comments.

