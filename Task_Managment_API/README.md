Task Management API

A Django REST Framework–based API that allows users to manage their tasks with authentication powered by JWT. Users can create, read, update, and delete tasks while keeping their data secure and private.

🚀 Features

User Authentication

Custom user model (CustomUser)

JWT authentication with access & refresh tokens

Task Management

Create, update, delete, and view tasks

Mark tasks as complete or incomplete

User-specific tasks (each user only sees their own tasks)

Security

Authentication required for all task operations

Permissions enforced with Django REST Framework

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


Run the development server:

    python manage.py runserver

🔑 Authentication

    Obtain JWT token:

POST /api/token/
{
  "username": "your_username",
  "password": "your_password"
}


Response:

{
  "refresh": "long-refresh-token",
  "access": "short-access-token"
}


Refresh token:

POST /api/token/refresh/
{
  "refresh": "long-refresh-token"
}

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

📄 License

This project is licensed under the MIT License.