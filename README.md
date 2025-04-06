# 🎓 Course Management System

A Django-based web application designed using the **MVCS (Model-View-Controller-Service)** clean architecture pattern. The system facilitates student registration, course creation by faculty, and enrollment management in a modular, maintainable, and scalable structure.

---

## 🧠 Architecture Overview

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

## 🚀 Features

### 👥 User Roles
- **Student**
  - Register and log in.
  - Browse and enroll in courses.
  - View enrolled courses.

- **Faculty**
  - Log in to view and manage assigned courses.
  - Create new courses with detailed info.
  - Monitor student enrollments.

---
