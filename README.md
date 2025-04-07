# Django Application Setup Guide

Follow the steps below to set up and run the Django application.

---

## 1. Create a Virtual Environment
To isolate the project dependencies, create a virtual environment:

```bash
python -m venv venv
```

## 2. Activate the virtual environment
```bash
venv\Scripts\activate
```

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 4. Apply migrations
```bash
python manage.py migrate
```

## 5. Run the Development Server
```bash
python manage.py runserver
```
