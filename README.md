## DjangoServer

A lightweight Django project scaffold intended for local development and experimentation. The repository contains a Django project named `JP` with a starter app `MiPrimeraPagina`. It runs on Django 5.x and Python 3.12 (a virtual environment is included in `venv/`).

### Features
- **Django 5.x** project configured with `JP/settings.py`
- Starter app: `MiPrimeraPagina`
- SQLite database for local development (`JP/db.sqlite3`)
- Ready-to-run local server with `manage.py`

### Tech Stack
- **Backend**: Django (Python)
- **Database**: SQLite (development)
- **Runtime**: Python 3.12

### Project Structure
```
DjangoServer/
  JP/
    JP/               # Django project (settings, urls, wsgi, asgi)
    MiPrimeraPagina/  # Example Django app
    manage.py         # Django management entry point
    db.sqlite3        # Local dev database (generated)
  venv/               # Python virtual environment
  README.md
```

### Prerequisites
- Python 3.12 installed
- PowerShell (Windows) or a POSIX shell (macOS/Linux)

### Setup
1) Clone or open the repository locally.

2) Create and activate a virtual environment (if you prefer a fresh one):
   - PowerShell (Windows):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - Bash (macOS/Linux):
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   Note: This repo already includes `venv/`. If you use it on Windows PowerShell, try one of:
   ```powershell
   .\venv\Scripts\Activate.ps1
   # or (depending on how it was created)
   .\venv\bin\Activate.ps1
   ```

3) Install dependencies (if starting clean):
   ```bash
   pip install --upgrade pip
   pip install django
   ```
   Optionally, freeze dependencies for reproducibility:
   ```bash
   pip freeze > requirements.txt
   ```

### Configuration
- Default settings are in `JP/JP/settings.py`.
- Database defaults to SQLite at `JP/db.sqlite3`.
- For local development, no additional environment variables are required. For production, configure environment variables and a production-ready database.

### Database Migrations
From the repository root, navigate into the Django project folder and run migrations:
```bash
cd JP
python manage.py migrate
```

### Running the Development Server
```bash
cd JP
python manage.py runserver
```
Then open `http://127.0.0.1:8000/` in your browser.

### Create an Admin Superuser (optional)
```bash
cd JP
python manage.py createsuperuser
```
Log in at `http://127.0.0.1:8000/admin/` after starting the server.

### Useful Commands
```bash
# Start app (example)
python manage.py startapp my_app

# Make and apply migrations
python manage.py makemigrations
python manage.py migrate

# Run tests
python manage.py test

# Collect static files (for production setups)
python manage.py collectstatic --noinput
```

### Troubleshooting
- If the virtual environment fails to activate on Windows, ensure PowerShell execution policy allows scripts:
  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```
- If `python` points to a different version, use `py -3.12` (Windows) or `python3` (macOS/Linux).

### License
This project is distributed for educational purposes. Add your preferred license text here if needed.

