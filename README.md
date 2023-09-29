# Task_Management_Backend
task_management_backend

Task Management Application
This is a task management application built with React for the frontend and Django for the backend.

## Technologies Used
- React
- Django
- Django REST Framework
- SQLite (or your preferred database)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Node.js and npm installed (for the React frontend)
- Python and pip installed (for the Django backend)

## Getting Started

### Frontend (React)
1. Navigate to the `frontend` directory:
       cd task-management-frontend

2. Install dependencies:
        npm i

3. Run the development server:
        npm start

### Backend (Django)

1. Navigate to the `backend` directory:
     cd task_management_backend

2. Create a virtual environment:
     python -m venv venv

3. Activate the virtual environment:
  - On Windows:
        bash
        .\venv\Scripts\activate
        
    - On macOS/Linux:
        bash
        source venv/bin/activate

4. Install dependencies:
    pip install -r requirements.txt

5. Apply database migrations:
    python manage.py makemigrations,
    python manage.py migrate

6. Run the development server:
    python manage.py runserver
    


