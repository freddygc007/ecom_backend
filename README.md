# E-commerce Backend

A Django-based e-commerce backend application with customer management, product catalog, and order processing.

## Project Structure

- `customers/` - Customer management and authentication
- `products/` - Product catalog and inventory management
- `orders/` - Order processing and management
- `themes/` - UI themes and styling
- `templates/` - HTML templates for the frontend
- `EcomBackend/` - Main Django project settings

## Setup Instructions

1. **Activate your virtual environment:**
   ```bash
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Features

- Customer registration and authentication
- Product catalog with categories
- Shopping cart functionality
- Order management
- Admin interface for managing products and orders

## Dependencies

- Django 5.2.5 - Web framework
- Pillow 10.4.0 - Image processing
- django-crispy-forms 2.1 - Form styling
- crispy-bootstrap5 2024.2 - Bootstrap 5 integration
- python-decouple 3.8 - Environment variable management
