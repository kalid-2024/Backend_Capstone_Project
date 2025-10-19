Task Management API

A Django REST Framework–based API that allows users to manage their tasks with authentication powered by JWT. Users can create, read, update, and delete tasks while keeping their data secure and private.

🚀 Features

# User Authentication
# Custom user model (CustomUser)
# JWT authentication with access & refresh tokens
# Task Management
# Create, update, delete, and view tasks
# Mark tasks as complete or incomplete
# User-specific tasks (each user only sees their own tasks)
# Security
# Authentication required for all task operations
# Permissions enforced with Django REST Framework

🛠️ Tech Stack
Backend: Django, Django REST Framework
Authentication: JWT (djangorestframework-simplejwt)
Database: SQLite (default, can be swapped for PostgreSQL/MySQL)
Language: Python 3.12+

📦 Installation
Clone the repository:
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies:

    pip install -r requirements.txt


Apply migrations:

    python manage.py makemigrations
    python manage.py migrate

Create a superuser:

    python manage.py createsuperuser


1️⃣ User Endpoints
    #Register a New User
      Method: POST
      URL: http://localhost:8000/api/users/register/
      Body (JSON):

    {
        "username": "testuser",
        "email": "testuser@gmail.com"
        "password": "testpass"
}

      Expected Response: 201 Created, user info returned.

    #Login (JWT Token)
      Method: POST
      URL: http://localhost:8000/api/users/login/

      Body (JSON):

  {
    "username": "testuser",
    "password": "testpass"
  }

      Expected Response: 200 OK, returns:

      {
        "refresh": "<refresh_token>",
        "access": "<access_token>"
      }


      Note: Copy the access token to use for authorized requests.

    #Get User Profile
      Method: GET
      URL: http://localhost:8000/api/users/profile/

      Headers:

      Authorization: Bearer <access_token>

      Expected Response: 200 OK, returns logged-in user details.

2️⃣ Task Endpoints

    Important: All task endpoints require Authorization: Bearer <access_token>

    #List Tasks
      Method: GET
      URL: http://localhost:8000/api/tasks/

      Headers:

      Authorization: Bearer <access_token>

      Expected Response: 200 OK, array of tasks for logged-in user.

    #Create a Task
      Method: POST
      URL: http://localhost:8000/api/tasks/

      Headers:

      Authorization: Bearer <access_token>

      Body (JSON):

{
  "title": "Prepare Monthly Financial Report",
  "description": "Compile the financial data for the month of October 2025. This includes gathering all invoices, expenses, and revenue records, analyzing discrepancies, preparing summary charts, and drafting the final report. Ensure the report follows the company's reporting standards and is ready for review by the finance manager.",
  "status": "pending",
  "priority": "high",
  "due_date": "2025-10-25"
}


      Expected Response: 201 Created, task details returned.

    Get Task Details
      Method: GET
      URL: http://localhost:8000/api/tasks/<id>/

      Headers:

      Authorization: Bearer <access_token>

      Expected Response: 200 OK, task detail returned.

    Update a Task
      Method: PUT
      URL: http://localhost:8000/api/tasks/<id>/

      Headers:

      Authorization: Bearer <access_token>

      Body (JSON):

      {
        "title": "Updated Task",
        "description": "Updated description",
        "status": "pending",
        "due_date": "2025-10-30"
      }

      Expected Response: 200 OK, updated task returned.

    Delete a Task
      Method: DELETE
      URL: http://localhost:8000/api/tasks/<id>/

      Headers:

      Authorization: Bearer <access_token>

      Expected Response: 204 No Content

    #Toggle Task Complete / Incomplete
      Method: PATCH
      URL: http://localhost:8000/api/tasks/<id>/complete/

      Headers:

      Authorization: Bearer <access_token>

      Body: Empty

      Expected Response: 200 OK, task status toggled between pending and completed.

📌 API Endpoints
| Method | Endpoint              | Description                       | Auth Required |
|--------|----------------------|-----------------------------------|---------------|
| POST   | /api/token/           | Obtain JWT access & refresh token | No            |
| POST   | /api/token/refresh/   | Refresh JWT token                 | No            |
| GET    | /api/tasks/           | List all tasks for logged-in user | Yes           |
| POST   | /api/tasks/           | Create a new task                 | Yes           |
| GET    | /api/tasks/{id}/      | Retrieve a specific task          | Yes           |
| PUT    | /api/tasks/{id}/      | Update a task                     | Yes           |
| DELETE | /api/tasks/{id}/      | Delete a task                     | Yes           |

✅ Example Task Object
{
  "id": 1,
  "title": "Finish Django project",
  "description": "Implement JWT authentication and CRUD operations",
  "completed": false,
  "owner": 1
}

🧪 Running Tests
python manage.py test

📌 Next Steps

Add user registration API endpoint

Improve test coverage

Add API documentation (Swagger/OpenAPI)

Deploy to cloud platform (Heroku/DigitalOcean)