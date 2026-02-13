#  FocusFlow — Productivity SaaS Backend (Django REST Framework)

FocusFlow is a multi-user productivity SaaS backend built using **Django** and **Django REST Framework (DRF)**.
The project demonstrates scalable backend architecture, secure API design, and real-world SaaS patterns.

---

##  Project Overview

FocusFlow allows users to organize work using a hierarchical structure:

User → Workspace → Project → Task

Each user can create workspaces, manage projects, track tasks, and view productivity analytics through a dashboard API.

This project was built to practice real backend engineering concepts such as:

* REST API architecture
* Authentication & permissions
* Relational data modeling
* API performance optimization

---

##  Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (development)
* django-filter

---

##  Features

###  Authentication & Permissions

* Authenticated API access
* Object-level permissions
* Owner-based data filtering

###  Core Modules

* Workspaces
* Projects
* Tasks
* Dashboard analytics

###  Advanced API Capabilities

* Pagination
* Filtering (`?is_completed=true`)
* Search (`?search=keyword`)
* Ordering (`?ordering=-created_at`)
* Custom actions (`mark_complete`)

###  Performance Improvements

* Optimized queries using `select_related`
* Clean serializer responses with nested fields

---

##  API Endpoints

### Workspaces

```
GET    /api/workspaces/
POST   /api/workspaces/
PATCH  /api/workspaces/{id}/
DELETE /api/workspaces/{id}/
```

### Projects

```
GET    /api/projects/
POST   /api/projects/
```

### Tasks

```
GET    /api/tasks/
POST   /api/tasks/
POST   /api/tasks/{id}/mark_complete/
```

### Dashboard

```
GET /api/dashboard/
```

---

## 🧪 Query Examples

Filter completed tasks:

```
/api/tasks/?is_completed=true
```

Search tasks:

```
/api/tasks/?search=array
```

Order tasks:

```
/api/tasks/?ordering=-created_at
```

---

## 🏗️ Project Structure

```
focusflow/
├── workspaces/
├── projects/
├── tasks/
├── dashboard/
└── config/
```

The project follows a **domain-based app structure** instead of a single API app, making it scalable and closer to real production backends.

---

## ▶️ Getting Started

### 1️⃣ Create virtual environment

```
python -m venv env
source env/Scripts/activate
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run migrations

```
python manage.py migrate
```

### 4️⃣ Start server

```
python manage.py runserver
```

---

## 🎯 Learning Goals

This project focuses on mastering:

* ModelViewSet vs APIView design
* Custom DRF actions
* Serializer customization
* Query optimization
* Clean API architecture

---

## 📌 Future Improvements

* Team collaboration system
* Role-based permissions
* JWT authentication
* Deployment (Docker / Render / AWS)

---

## 👨‍💻 Author

Kunal Yadav
Backend Developer (Django + DRF)
