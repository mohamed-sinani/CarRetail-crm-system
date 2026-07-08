# Car Retail CRM Deployment

## Project Structure

- `accounts` custom users, roles, login/logout, default account seed
- `dashboard` analytics dashboard and marketing overview
- `vehicles` inventory management
- `customers` contact profiles and assigned salesperson
- `deals` Kanban sales pipeline
- `sales` transaction tracking and automatic sold status updates
- `announcements` internal dealership announcements
- `reports` sales, inventory, and revenue report exports
- `templates` shared Bootstrap 5 templates
- `static` CRM CSS and JavaScript/Chart.js wiring

## PostgreSQL Configuration

Set these environment variables in production:

```bash
export POSTGRES_DB=carretail
export POSTGRES_USER=carretail
export POSTGRES_PASSWORD='change-me'
export POSTGRES_HOST=127.0.0.1
export POSTGRES_PORT=5432
export DJANGO_ALLOWED_HOSTS='your-domain.com,127.0.0.1'
```

If `POSTGRES_DB` is not set, the project falls back to SQLite for local development.

## Install And Run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_defaults
python manage.py collectstatic
gunicorn carretail.wsgi:application
```

Default accounts are also created automatically after migrations:

- `admin` / `admin123`
- `marketing` / `marketing123`
- `sales` / `sales123`

## Existing SQLite Note

This repository previously had a starter `db.sqlite3` created before the custom user model. If local migration reports inconsistent migration history, move that old development database aside and run migrations on a fresh database:

```bash
mv db.sqlite3 db.sqlite3.backup
python manage.py migrate
```
