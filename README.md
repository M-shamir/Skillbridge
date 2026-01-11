
# SkillBridge Backend

> **Note (Linux):** If PostgreSQL is running locally and conflicts with Docker, stop it:
>
> ```bash
> sudo service postgresql stop
> ```

SkillBridge is a backend service built with **Django REST Framework**, **PostgreSQL**, and **Docker**. It provides APIs for authentication, user management, and platform-specific features, all containerized for easy development and deployment.

---

## 🚀 Tech Stack

* **Backend:** Django 6 + Django REST Framework
* **Database:** PostgreSQL
* **Authentication:** JWT (SimpleJWT)
* **Containerization:** Docker & Docker Compose
* **ASGI:** Uvicorn + Channels (optional)

---

## 📦 Project Structure (simplified)

```
skillbridge-backend/
├── core/
├── users/
├── beneficiaries/
├── trianers/
├── trainer-session/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:

```
DEBUG=1
SECRET_KEY=your-secret-key
POSTGRES_DB=skillbridge_dbone
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

# SMTP Email (example: Gmail)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=1
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=SkillBridge <your-email@gmail.com>
```

---

## 🐳 Docker Setup

### Build and start containers

```bash
docker compose up -d --build
```

### Apply migrations

```bash
docker compose exec web python manage.py migrate
```

### Create superuser

```bash
docker compose exec web python manage.py createsuperuser
```

---

## 🔐 Authentication

SkillBridge uses **JWT authentication**.

* Login endpoint returns `access` and `refresh` tokens
* Include token in headers:

```
Authorization: Bearer <access_token>
```

---

## 🌐 API Base URL

```
http://localhost:8000/api/v1/
```

Example endpoints:

* `POST /auth/login/`
* `POST /auth/register/`
* `POST /beneficiaries/approve/`

---

## 🔄 Common Commands

```bash
# Stop containers
docker compose down

# Stop and remove volumes (reset DB)
docker compose down -v

# View logs
docker compose logs -f
```

---

## ✅ Notes

* PostgreSQL database is created automatically by Docker
* Do NOT change `POSTGRES_DB` without recreating volumes
* `makemigrations` does not touch the database; use `migrate`

---

## 📌 Development Tips

* Use `.env` for secrets
* Keep DB config in sync with Docker
* Rebuild containers after dependency changes

---

## 🧑‍💻 Author

SkillBridge Backend — Django REST API

---

Happy coding 🚀
