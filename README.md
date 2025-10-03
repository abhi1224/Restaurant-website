# Restaurant Management Web Application

A full-stack web application built with **Django** for managing restaurant operations including user registration, product browsing, order placement, and customer inquiries.

---

## Features

- **User Management**
  - Register new users with username, email, and password.
  - Login and logout functionality using Django authentication.
  
- **Product Management**
  - Browse all available products.
  - View detailed information for each product.

- **Order Management**
  - Place orders with product, quantity, and price details.
  - Orders are saved in the database with user and product information.
  - Success and error messages displayed upon order placement.

- **Contact Form**
  - Users can submit inquiries or feedback.
  - Messages stored in the database with user information and submission date.
  - Confirmation messages displayed after submission.

- **Static Pages**
  - Home, About, Dashboard, and Welcome pages for smooth navigation and better user experience.

---

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default Django DB)
- **Authentication:** Django built-in `User` model

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abhi1224/Restaurant-website.git

2. Run the development server:
   ```bash
    python manage.py runserver
   
3. Open your browser and go to http://127.0.0.1:8000/

 
