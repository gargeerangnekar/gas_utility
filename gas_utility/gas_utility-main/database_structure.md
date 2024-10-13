
# Database Structure for Gas Utility Service

## Tables

### 1. `auth_user`
This table is provided by Django's built-in authentication system to manage users.

| Column      | Type       | Description                            |
|-------------|------------|----------------------------------------|
| id          | Integer    | Primary Key                            |
| username    | CharField  | Unique Username                        |
| email       | CharField  | User's Email                           |
| password    | CharField  | Hashed Password                        |
| first_name  | CharField  | User's First Name                      |
| last_name   | CharField  | User's Last Name                       |
| is_staff    | Boolean    | Indicates if the user is an admin      |

---

### 2. `service_account`
This table stores account information for each user.

| Column        | Type       | Description                            |
|---------------|------------|----------------------------------------|
| id            | Integer    | Primary Key                            |
| user_id       | ForeignKey | References `auth_user`                 |
| account_number| CharField  | Unique Account Number                  |
| address       | CharField  | Customer's Address                     |
| phone_number  | CharField  | Customer's Phone Number                |

---

### 3. `service_servicerequest`
This table stores customer service requests.

| Column       | Type        | Description                            |
|--------------|-------------|----------------------------------------|
| id           | Integer     | Primary Key                            |
| user_id      | ForeignKey  | References `auth_user`                 |
| request_type | CharField   | Type of Service Request (e.g. Gas Leak)|
| description  | TextField   | Details of the request                 |
| status       | CharField   | Status of the request (e.g. Pending)   |
| created_at   | DateTime    | When the request was created           |
| updated_at   | DateTime    | When the request was last updated      |
| attachment   | FileField   | Attachment file                        |

---

### 4. `service_notification`
This table stores notifications for users regarding service request updates.

| Column      | Type        | Description                            |
|-------------|-------------|----------------------------------------|
| id          | Integer     | Primary Key                            |
| user_id     | ForeignKey  | References `auth_user`                 |
| message     | CharField   | The notification message               |
| created_at  | DateTime    | When the notification was created      |
| is_read     | Boolean     | Whether the notification has been read |

---

### 5. `service_comment`
This table stores comments made on service requests.

| Column      | Type        | Description                            |
|-------------|-------------|----------------------------------------|
| id          | Integer     | Primary Key                            |
| request_id  | ForeignKey  | References `service_servicerequest`     |
| user_id     | ForeignKey  | References `auth_user`                 |
| message     | TextField   | Comment text                           |
| created_at  | DateTime    | When the comment was made              |

---

## Example Data Structure:

### Table: `auth_user`
| id  | username  | email          | password | first_name | last_name | is_staff |
| --- | --------- | -------------- | -------- | ---------- | --------- | -------- |
| 1   | testuser  | test@user.com  | ***      | John       | Doe       | False    |
| 2   | adminuser | admin@user.com | ***      | Admin      | Smith     | True     |

### Table: `service_account`
| id  | user_id | account_number | address           | phone_number |
| --- | ------- | -------------- | ----------------- | ------------ |
| 1   | 1       | 123456         | 123 Main St       | 555-1234     |

### Table: `service_servicerequest`
| id  | user_id | request_type | description       | status  | created_at          | updated_at          | attachment |
| --- | ------- | ------------ | ----------------- | ------- | ------------------- | ------------------- | ---------- |
| 1   | 1       | gas_leak     | Gas leak in kitchen | Pending | 2024-10-10 10:00:00 | 2024-10-10 10:00:00 | NULL       |
| 2   | 1       | maintenance  | Routine check-up  | Resolved| 2024-10-09 09:00:00 | 2024-10-09 12:00:00 | NULL       |

### Table: `service_notification`
| id  | user_id | message                                     | created_at          | is_read |
| --- | ------- | ------------------------------------------- | ------------------- | ------- |
| 1   | 1       | Your service request "Gas Leak" is pending. | 2024-10-10 10:01:00 | False   |

### Table: `service_comment`
| id  | request_id | user_id | message              | created_at          |
| --- | ---------- | ------- | -------------------- | ------------------- |
| 1   | 1          | 1       | Please fix this ASAP | 2024-10-10 10:05:00 |
