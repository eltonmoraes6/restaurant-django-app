# 🍔 Django Restaurant Ordering System

A full-featured restaurant web application built with **Django**, including menu browsing, cart, checkout, orders, user profiles, and an admin dashboard.

---

# 🚀 Features

* User authentication (login, signup, logout)
* Menu browsing with categories
* Add to cart (AJAX modal + full cart page)
* Checkout and order creation
* User Profile page
* My Orders page
* Admin Dashboard (for staff users)
* Table Booking system
* Feedback submission
* Responsive Bootstrap theme

---

# 🛠️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/eltonmoraes6/restaurant-django-app.git
cd restaurant-django-app
```

---

## 2️⃣ Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# ⭐ 5️⃣ Create an Admin User (Superuser)

You have **two options**:

---

## **Option A: Create manually**

```bash
python manage.py createsuperuser
```

---

## **Option B: Auto-create superuser (recommended for deployments)**

Create a file:

### `create_admin.py`

```python
from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
email = "admin@example.com"
password = "admin123"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created automatically.")
else:
    print("Superuser already exists.")
```

Then run:

```bash
python manage.py shell < create_admin.py
```

---

# ▶️ 6️⃣ Start the Application

```bash
python manage.py runserver
```

Your application will be available at:

👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Admin panel:

👉 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

# ⚙️ Configuration

## Static Files

```bash
python manage.py collectstatic
```

---

## Environment Variables (optional)

Create `.env`:

```
SECRET_KEY=your-secret-key
DEBUG=True
```

---

# 🗄️ Database (SQLite / PostgreSQL)

SQLite works out of the box.

To use PostgreSQL:

```bash
pip install psycopg2
```

Modify `DATABASES` in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restaurant_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Apply migrations again:

```bash
python manage.py migrate
```

---

# 🧪 Tests

```bash
python manage.py test
```

---

# 🚀 Deployment Notes

Production services require:

```
pip install gunicorn whitenoise
```

Add Whitenoise to `MIDDLEWARE`:

```python
"whitenoise.middleware.WhiteNoiseMiddleware",
```

Run production server:

```bash
gunicorn project_name.wsgi
```

