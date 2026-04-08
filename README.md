#  Simple CRUD — Django

<div align="center">

**A simple and clean CRUD application built with Django & Python**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![GitHub Stars](https://img.shields.io/github/stars/bahasalah255/Simple-Crud-Django?style=for-the-badge)](https://github.com/bahasalah255/Simple-Crud-Django/stargazers)

</div>

---

## 📖 About

**Simple-Crud-Django** is a beginner-friendly Django project demonstrating the four core database operations — **Create, Read, Update, Delete (CRUD)**. It's a great starting point for learning Django's MVT architecture, URL routing, views, models, and templates.

---

## ✨ Features

- ➕ **Create** — Add new records via a form
- 📋 **Read** — List and view all records
- ✏️ **Update** — Edit existing records
- 🗑️ **Delete** — Remove records with confirmation
- 🗄️ SQLite database (zero config, built-in)
- 🧩 Django MVT architecture (Models, Views, Templates)

---

## 🛠️ Tech Stack

| Technology | Role |
|------------|------|
| Python | Backend language |
| Django | Web framework |
| SQLite | Database |
| HTML5 | Templates & UI |

---

## 📂 Project Structure

```
Simple-Crud-Django/
│
└── project/
    └── test/
        ├── manage.py
        ├── db.sqlite3
        ├── project/          # Django project settings
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── test/             # Main app
            ├── models.py     # Data models
            ├── views.py      # Business logic
            ├── urls.py       # URL routing
            ├── forms.py      # Django forms
            ├── admin.py      # Admin panel config
            └── templates/    # HTML templates
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/bahasalah255/Simple-Crud-Django.git
   cd Simple-Crud-Django/project/test
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux / macOS
   venv\Scripts\activate          # Windows
   ```

3. **Install Django**
   ```bash
   pip install django
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

---

## 🔑 Admin Panel

Create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Then visit: `http://127.0.0.1:8000/admin/`

---

## 📌 What I Learned

- Django project & app structure
- Defining models and running migrations
- Creating views (function-based)
- URL routing with `urls.py`
- Using Django forms for data input
- Rendering HTML templates with context data

---

## 🔭 Future Improvements

- [ ] Add user authentication
- [ ] Style with Bootstrap or Tailwind CSS
- [ ] Pagination for list views
- [ ] Search & filter functionality
- [ ] REST API version with Django REST Framework

---

## 👨‍💻 Author

**Salah Baha**
🔗 GitHub: [@bahasalah255](https://github.com/bahasalah255)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

⭐ If this helped you learn Django, consider giving it a star!

</div>
