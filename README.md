<div align="center">

# 📁 File Management System

### A role-based file tracking & management web application built with Django

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Coming_Soon-orange?style=for-the-badge)](https://github.com/ryzenop07/FIle_Management_System)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/ryzenop07/FIle_Management_System)
[![Commits](https://img.shields.io/badge/Total_Commits-7-blue?style=for-the-badge&logo=git)](https://github.com/ryzenop07/FIle_Management_System/commits/main)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django)](https://djangoproject.com)

</div>

---

## 🚀 Live Demo

> 🔗 **Live Link:** _Will be updated after deployment_

---

## 📌 About The Project

**File Management System (FMS)** is a full-stack web application that allows organizations to manage, track, and forward files/documents between departments and employees. It features a dual-role system — **Admin** and **User** — with separate dashboards and access controls.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔐 Admin Login | Secure admin authentication with session management |
| 👥 Employee Management | Add, view, and manage employees with roles & departments |
| 🏢 Department Management | Create and manage departments with head & contact info |
| 📄 File Upload & Tracking | Upload files with priority, assign to departments/users |
| 🔄 File Forwarding | Track file movement between users with status updates |
| 📥 Received Files | View files received by admin and users |
| 👤 User Dashboard | Separate portal for employees to manage their files |
| 📝 User Create File | Users can create and submit files from their portal |
| 📬 User Received Files | Users can view files received in their portal |
| 🖼️ Profile Photos | Employee photo upload support |

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite3
- **Auth:** Django Session-based Authentication

---

## 📂 Project Structure

```
fms/
├── fms/                  # Django project settings
├── myapp/
│   ├── models.py         # DB models: Admin, Department, Employee, File
│   ├── views.py          # All business logic & request handling
│   ├── urls.py           # URL routing
│   └── templates/
│       ├── admin/        # Admin panel templates
│       └── user/         # User portal templates
├── media/                # Uploaded files & profile photos (not tracked in git)
├── .gitignore
└── manage.py
```

---

## 🗄️ Database Models

- **adminlogin** — Admin credentials
- **adddepartment** — Department info (name, code, head, email, contact)
- **Empadd** — Employee records (name, role, department, designation, photo)
- **Fileupload** — File records (file no, subject, priority, department, status)

---

## ⚙️ Local Setup

```bash
git clone https://github.com/ryzenop07/FIle_Management_System.git
cd FIle_Management_System/fms
pip install django pillow
python manage.py migrate
python manage.py runserver
```

Visit: `http://127.0.0.1:8000`

---

## 📈 Development Progress

- [x] Admin login & session management
- [x] Department CRUD
- [x] Employee management with photo upload
- [x] File upload with priority & department assignment
- [x] User login & role-based access
- [x] User create file from user portal
- [x] User received files view
- [x] Admin received files view
- [ ] File forwarding history/timeline
- [ ] Email notifications
- [ ] Deployment (Live link coming soon)

---

## 👨‍💻 Developer

**Vishal Prajapati**
[![GitHub](https://img.shields.io/badge/GitHub-ryzenop07-181717?style=flat&logo=github)](https://github.com/ryzenop07)

---

<div align="center">
⭐ Star this repo if you found it useful!
</div>
