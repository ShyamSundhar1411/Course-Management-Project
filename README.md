# 🎓 Course Management System

A Django-based web application designed using the **MVCS (Model-View-Controller-Service)** clean architecture pattern. The system facilitates student registration, course creation by faculty, and enrollment management in a modular, maintainable, and scalable structure.

---

## Architecture Overview

This project follows a **clean architecture** based on the **MVCS pattern**, promoting **separation of concerns** and testability.

### 📦 Layers
- **Models**: Define the database structure (e.g., `Student`, `Faculty`, `Course`, `Enrollment`).
- **Views (Controllers)**: Handle HTTP requests and orchestrate logic via services.
- **Services**: Encapsulate business logic (e.g., course creation, enrollment validation).
- **Forms**: Manage user input and validation.
- **Infrastructure**: Manage Low Level Database interactions and acts as a wrapper of model functions with improvised error handling.
- **Templates**: Handle presentation logic using Django templating and Bootstrap.
- **Utilities**: Store constants, messages, and reusable logic.

> ✅ All business logic lives in `services/`, keeping views thin and focused on request/response handling.

---

## Features

### User Roles
- **Student**
  - Register and log in.
  - Browse and enroll in courses.
  - View enrolled courses.

- **Faculty**
  - Log in to view and manage assigned courses.
  - Create new courses with detailed info.
  - Monitor student enrollments.

---

## How to Run Locally

### Prerequisites

- Python 3.11+ installed
- Poetry installed (https://python-poetry.org/docs/)
- PostgreSQL installed and running

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/ShyamSundhar1411/Course-Management-Project.git
cd Course-Management-Project
```

2. **Setup environment variables**

Create a `.env` file in the root directory with the following content (adjust as needed):

```
DATABASE_NAME=db_name
DATABASE_USER=your_username
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

3. **Install dependencies with Poetry**

```bash
poetry install
```

4. **Activate Poetry shell**

```bash
poetry shell
```

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Create a superuser (optional)**

```bash
python manage.py createsuperuser
```

7. **Run the development server**

```bash
python manage.py runserver
```

8. **Access the application**

Open your browser and navigate to http://localhost:8000

---


For full source code, visit the [GitHub repository](https://github.com/ShyamSundhar1411/Course-Management-Project).
