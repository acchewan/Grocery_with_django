# Grocery Bud - Django Edition

A sleek, responsive grocery list application built with **Django** and vanilla **CSS**. 

![App Preview](https://grocery-with-django-1.onrender.com/static/grocery/images/preview.png)

## Features
- **Full CRUD**: Add, Edit, Toggle, and Delete items.
- **Clear All**: Reset your list with a single click.
- **Item Counter**: Stay on top of your tasks with a live item badge.
- **Responsive Design**: optimized for desktop and mobile.
- **Django Admin**: Managed interface for data oversight.
- **Deployment Ready**: Configured for Render with Gunicorn and WhiteNoise.

## Local Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/acchewan/Grocery_with_django.git
   cd Grocery_with_django
   ```

2. **Setup Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start Dev Server**
   ```bash
   python manage.py runserver
   ```

## Deployment steps (Render)

1. Connect repo to Render.
2. Set Build Command: `bash build.sh`
3. Set Start Command: `gunicorn djangocrud.wsgi`
4. Add environment variables: `SECRET_KEY`, `DEBUG=False`.

## License
MIT
