# Django Login Signup With WAMPServer

This project uses Django authentication for signup, login, logout, and a protected dashboard.

## WAMPServer database setup

1. Start WAMPServer and make sure the MySQL service is green/running.
2. Open phpMyAdmin and confirm your MySQL username/password.
3. Create the database:

```sql
CREATE DATABASE IF NOT EXISTS django_login_app
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
```

You can also run the same SQL from `database_setup.sql`.

## Run migrations

If your WAMP MySQL root user has no password:

```powershell
python manage.py migrate
python manage.py runserver
```

If your WAMP MySQL root user has a password:

```powershell
$env:MYSQL_PASSWORD="your_mysql_password"
python manage.py migrate
python manage.py runserver
```

After signing up in the browser, open phpMyAdmin and check the `django_login_app` database. Django creates tables such as `auth_user`, `django_session`, and `django_migrations`; new signup users appear in `auth_user`.
