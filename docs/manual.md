# 🍽️ **Restaurant Web Application – Complete User & Developer Manual**

**Version:** 1.0.0
**Framework:** Django 5.2
**Audience:** End Users, Administrators, Developers
**Author:** Elton Moraes

---

# 📚 **Table of Contents**

1. [Introduction](#-1-introduction)
2. [Application Structure](#-2-understanding-the-application-structure)
3. [User Guide](#-3-using-the-application-user-guide)

   - Home Page
   - Menu
   - Cart
   - Checkout
   - Orders
   - Profile
   - Feedback
   - Booking Tables

4. [Admin Guide](#-4-admin-guide)
5. [Developer Guide](#-5-developer-guide-full)

   - Installation
   - Project Structure
   - Models
   - Routing
   - APIs
   - Debugging
   - Deployment

6. [Adding Images](#-6-tips-for-adding-images-later)
7. [Conclusion](#-manual-complete)

---

# ⭐ **1. Introduction**

The Restaurant Web Application is a full-featured Django system designed for:

🍔 Displaying restaurant menu items
🛒 Adding items to a cart
💳 Online ordering
📦 Order tracking
👤 User profile management
🛠 Admin dashboard for restaurant management
📅 Table booking
⭐ Customer feedback system

This document explains **how to use the application** as a customer and **how to manage it as an administrator**, followed by a **complete developer guide**.

---

# ⭐ **2. Understanding the Application Structure**

The system has three access levels:

---

## 🔓 Public Pages

Accessible without login:

- Home
- Menu
- About
- Feedback
- Book Table
- Contact
- Login & Register

---

## 🔐 Authenticated User Pages

Require account login:

- Cart
- Checkout
- My Orders
- User Profile
- Logout

---

## 🛠 Admin Pages (staff only)

Require:

```python
user.is_staff = True
```

Includes:

- Admin Dashboard
- Manage Orders
- Manage Menu Items
- Manage Users
- Manage Table Bookings
- Manage Feedback

---

# ⭐ **3. Using the Application (User Guide)**

Below are step-by-step instructions for **every screen** the customer interacts with.

---

## 📍 3.1 **Home Page**

Displayed when entering the site.

Includes:

- Large welcoming hero banner
- Restaurant highlights
- Featured dishes
- Testimonials
- Links to booking and ordering

![Menu Page](images/menu.png)

```

---

## 📍 3.2 **Navigation Menu**

Top navigation bar shows:

| Button         | Description                         |
| -------------- | ----------------------------------- |
| Home           | Main landing page                   |
| Menu           | Shows all dishes                    |
| About          | About the restaurant                |
| Book Table     | Reservation page                    |
| Feedback       | Leave review                        |
| Login/Register | Authentication                      |
| Cart           | Opens user shopping cart            |
| User Dropdown  | Profile, My Orders, Admin Dashboard |

```

![navigation_menu](images/menu-3.png)

```

---

## 🍔 3.3 **Menu Page – Browsing Items**

Shows food items with:

- Photo
- Title
- Description
- Price
- Add to Cart button

User actions:

1. Scroll through categories
2. Click **Add to Cart**
3. Confirmation message appears

```

[IMAGE: menu_page]

```

---

# 🛒 3.4 **Shopping Cart Page**

Displays a list of all items the user added.

### Includes:

- Item name
- Price
- Quantity (modify using + / – buttons)
- Total per item
- Remove button
- Grand total
- Checkout button

```

![cart_page](images/cart.png)

```

### Actions:

- ➕ Increase quantity
- ➖ Decrease quantity
- ❌ Remove item
- ✔ Proceed to Checkout

---

# 💳 3.5 **Checkout Page**

Summarizes the order:

- Items
- Quantities
- Prices
- Grand Total
- Place Order button

On clicking **Place Order**:

- Order object is created
- OrderItem objects are created
- Cart automatically clears
- User sees **Order Summary**

```

![checkout_page](images/checkout.png)

```

---

# 📦 3.6 **Order Summary Page**

Shows:

- Order number
- Date
- Payment status
- All items purchased
- Total price

```

![order_summary](images/order_summary.png)

```

---

# 📑 3.7 **My Orders Page**

History of all orders the user has made.

Each entry contains:

- Order ID
- Total amount
- Date
- Payment status
- View Details button

```

![my_orders_page](images/my_orders_page.png)

```

---

# 👤 3.8 **User Profile Page**

Shows:

- Username
- Email
- Join date
- Total orders

```

![profile_page](images/profile.png)

```

Future features can include editable fields such as phone, address, avatar, etc.

---

# ⭐ 3.9 **Feedback Page**

Form includes:

- Name
- Rating
- Message
- Optional Photo

Appears on the home page carousel.

```

![feedback_form](images/feedback_form.png)

```

---

# 🍽 3.10 **Table Booking Page**

Reservation form with:

- Name
- Phone
- Email
- Number of people
- Date

```

![table_booking](images/table_booking.png)

```

Bookings are automatically saved for admin review.

---

# ⭐ **4. Admin Guide**

Accessible only for staff users.

---

## 🛠 4.1 **Admin Dashboard**

Central management panel showing:

- Total Users
- Total Orders
- Total Menu Items
- Total Reservations
- Total Feedback

```

![admin_dashboard](images/admin_dashboard.png)

```

---

## 🍔 4.2 **Manage Menu Items**

Admin can:

- Add new items
- Upload images
- Edit items
- Delete items
- Add categories

```

[IMAGE: admin_menu_crud]

````

---

## 🧾 4.3 **Manage Orders**

Admin sees:

- Order ID
- Customer
- Total
- All items
- Payment status

Admin may update status such as completed, pending, refunded (optional).

---

## 🍽 4.4 **Manage Table Bookings**

Admin can see all bookings and change status if needed.

---

# ⭐ **5. Developer Guide (FULL)**

This section merges the complete README and expands it into a professional development manual.

---

## 🛠 5.1 Installation Steps

### Clone the repository:

```bash
git clone https://github.com/eltonmoraes6/restaurant-django-app.git
cd restaurant-django-app
````

---

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Create Superuser

```bash
python manage.py createsuperuser
```

**OR auto-create:**

```bash
python manage.py shell < create_admin.py
```

---

### Start Server

```bash
python manage.py runserver
```

App:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
Admin:
👉 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🧱 5.2 Project Structure

```
restaurant-django-app/
│
├── Base_App/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   ├── static/
│   ├── forms.py
│
├── Resturant_Project/
│   ├── settings.py
│   ├── urls.py
│
├── media/
├── static/
├── requirements.txt
└── README.md
```

---

## 🧩 5.3 Models Summary

- **Items** – menu dishes
- **Cart** – temporary storage before checkout
- **Order + OrderItem** – persistent purchase history
- **BookTable** – reservations
- **Feedback** – customer testimonials

---

## 🧭 5.4 Routing Overview

### Cart Operations

| URL               | View              |
| ----------------- | ----------------- |
| `/add-to-cart/`   | add_to_cart       |
| `/cart/`          | Cart_Page         |
| `/increase/<id>/` | increase_quantity |
| `/decrease/<id>/` | decrease_quantity |

---

## 🌐 5.5 API Behavior

### Example Cart Add Response

```json
{
  "message": "Item added successfully",
  "quantity": 1
}
```

---

## 🧪 5.6 Running Tests

```bash
python manage.py test
```

---

## 🐞 5.7 Debugging Tips

| Error                | Fix                              |
| -------------------- | -------------------------------- |
| NoReverseMatch       | URL name incorrect               |
| ImportError          | Wrong import path                |
| TemplateDoesNotExist | Template directory misconfigured |

---

## 🚀 5.8 Deployment Guide

Install for production:

```bash
pip install gunicorn whitenoise
```

Add to middleware:

```python
"whitenoise.middleware.WhiteNoiseMiddleware",
```

Run:

```bash
gunicorn Resturant_Project.wsgi
```

---

# ⭐ **6. Tips for Adding Images Later**

Wherever you see:

```
[IMAGE: menu_page]docs/images/menu.png
```

You can insert:

```markdown
![Menu Page](images/menu.png)
```

![Menu Page](images/menu.png)
I can also generate an `/images/` folder structure.

---
