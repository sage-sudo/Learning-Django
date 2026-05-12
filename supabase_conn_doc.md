# Supabase Connection Documentation
## Learning-Django Project

**Last Updated:** May 12, 2026

---

## Overview
The Learning-Django project is connected to **Supabase** for database management. Supabase provides a PostgreSQL database hosted on AWS infrastructure in the EU-West-1 region.

---

## Connection Configuration

### Database Engine
- **Type:** PostgreSQL (via Supabase)
- **Django Backend:** `django.db.backends.postgresql`
- **Location:** [my_tennis_club/my_tennis_club/settings.py](my_tennis_club/my_tennis_club/settings.py#L82-L105)

### Connection Details

#### Primary Configuration (IPv4 - Active)
```
HOST:     aws-0-eu-west-1.pooler.supabase.com
PORT:     5432
DATABASE: postgres
USER:     postgres.oxtncvjocwnhgzoxodvp
PASSWORD: [Configured in settings.py]
SSL Mode: require
```

#### Secondary Configuration (IPv6 - Fallback)
```
HOST:     aws-0-eu-west-1.pooler.supabase.com
PORT:     6543
DATABASE: postgres
USER:     postgres.oxtncvjocwnhgzoxodvp
PASSWORD: [Configured in settings.py]
SSL Mode: require
```

### Connection Switching Logic
The connection mode is controlled by the `IPV_4` variable in settings.py:
- **When `IPV_4 = True`:** Uses port 5432 (IPv4 - Primary)
- **When `IPV_4 = False`:** Uses port 6543 (IPv6 - Fallback)

Currently: **`IPV_4 = True`** (IPv4 is active)

---

## Credentials & Security

### Authentication
- **User ID Format:** `postgres.oxtncvjocwnhgzoxodvp` (Supabase's unique user format)
- **Region:** EU West 1 (Ireland)
- **Connection Pooling:** Enabled via Supabase's connection pooler (`pooler.supabase.com`)

### SSL/TLS
- **SSL Mode:** `require` - All connections must use SSL encryption
- **Purpose:** Ensures secure communication between Django and Supabase database

### Database Access
- **SQLite Fallback:** A commented-out SQLite configuration exists but is not used in production
- **Current Production:** PostgreSQL via Supabase only

---

## Django Models & Database Usage

### Connected Models
All models in the `members` app utilize the Supabase PostgreSQL database:

#### Member Model
**Location:** [members/models.py](my_tennis_club/members/models.py)

```python
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
```

**Migrations:**
- `0001_initial.py` - Initial table creation
- `0002_remove_member_email_member_joined_date_member_phone.py` - Schema modifications

---

## Database Operations

### Views Using Database Queries
The following views interact with the Supabase database through Django ORM:

1. **members()** - Retrieves all members
   ```python
   mymembers = Member.objects.all().values()
   ```

2. **details(id)** - Retrieves specific member by ID
   ```python
   mymember = Member.objects.get(id=id)
   ```

3. **testing()** - Test view for member retrieval
   ```python
   mymembers = Member.objects.all().values()
   ```

**Location:** [members/views.py](my_tennis_club/members/views.py)

---

## Database Applications

### Installed Apps Using Supabase
- **members** - Custom app for managing tennis club members
- **django.contrib.auth** - Django authentication (stores users)
- **django.contrib.contenttypes** - Content type framework
- **django.contrib.sessions** - Session management
- **django.contrib.admin** - Admin interface

---

## Settings Configuration Summary

**File:** [my_tennis_club/settings.py](my_tennis_club/my_tennis_club/settings.py)

| Setting | Value |
|---------|-------|
| DATABASE ENGINE | django.db.backends.postgresql |
| DATABASE NAME | postgres |
| DATABASE USER | postgres.oxtncvjocwnhgzoxodvp |
| DATABASE HOST | aws-0-eu-west-1.pooler.supabase.com |
| DATABASE PORT (IPv4) | 5432 |
| DATABASE PORT (IPv6) | 6543 |
| SSL MODE | require |
| DEBUG MODE | True |

---

## How to Use the Database

### Running Migrations
```bash
python manage.py migrate
```
This applies all migrations to the Supabase PostgreSQL database.

### Creating a New Member
```python
from members.models import Member
Member.objects.create(
    firstname="John",
    lastname="Doe",
    phone=1234567890,
    joined_date="2024-05-12"
)
```

### Querying Members
```python
# All members
all_members = Member.objects.all()

# By ID
member = Member.objects.get(id=1)

# By name
member = Member.objects.filter(firstname="John")
```

### Admin Interface
Access via: `http://localhost:8000/admin/`

---

## Connection Flow Diagram

```
Django Application (Django ORM)
        ↓
DatabaseRouter (settings.py)
        ↓
PostgreSQL Backend (django.db.backends.postgresql)
        ↓
SSL Encryption Layer (sslmode=require)
        ↓
Connection Pooler (pooler.supabase.com)
        ↓
Supabase PostgreSQL Instance (AWS EU-West-1)
```

---

## Troubleshooting

### Connection Issues
1. **Check SSL Mode:** Ensure `'sslmode': 'require'` is set
2. **Verify Credentials:** Double-check USER and PASSWORD in settings.py
3. **IPv4/IPv6 Toggle:** Try changing `IPV_4` variable if connection fails
4. **Port Availability:** Ensure port 5432 or 6543 is accessible

### Migration Issues
```bash
# Check migration status
python manage.py showmigrations

# Rollback if needed
python manage.py migrate members 0001
```

---

## Environment & Version Info

- **Django Version:** 6.0.3
- **Database:** PostgreSQL (via Supabase)
- **Middleware:** WhiteNoise (static file serving)
- **Server:** Django development server (`runserver`)

---

## Security Notes

⚠️ **Important:**
- Database credentials are currently hardcoded in settings.py
- **RECOMMENDATION:** Use environment variables instead:
  ```python
  import os
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': os.getenv('DB_NAME'),
          'USER': os.getenv('DB_USER'),
          'PASSWORD': os.getenv('DB_PASSWORD'),
          'HOST': os.getenv('DB_HOST'),
          'PORT': os.getenv('DB_PORT'),
          'OPTIONS': {
              'sslmode': 'require',
          },
      }
  }
  ```

- **Never commit sensitive credentials** to version control
- Use `.env` file or environment variables in production
- Rotate password periodically through Supabase dashboard

---

## Related Resources

- **Supabase Region:** AWS EU-West-1 (Ireland)
- **Project Type:** Learning/Educational Django Project
- **Main App:** Members Management System
- **Templates Location:** [members/templates/](my_tennis_club/members/templates/)
- **Static Files:** [mystaticfiles/](my_tennis_club/mystaticfiles/), [productionfiles/](my_tennis_club/productionfiles/)

---

## Conclusion

This Learning-Django project uses Supabase as its primary database backend for storing member information. The connection is configured with SSL encryption for security, and uses connection pooling for efficient resource management. The project demonstrates a practical implementation of Django ORM with a remote PostgreSQL database.
