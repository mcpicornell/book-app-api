📚 Book App API
This is the backend API for the Book App project, built with Django and MariaDB, containerized using Docker.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-user/book-app-api.git
cd book-app-api
````


### 2. Build the Docker containers
Before running the project, make sure to build the images:
```bash
docker-compose build --no-cache
````


### 3. Start the containers
Once built, you can start the containers:
```bash
docker-compose up
````

## This will:

- Start the database container

- Run migrations

- Seed users and books

- Start the Django development server at http://localhost:8080


# 🔄 If it fails the first time...

You may encounter an error the first time you run the app. This usually happens because the database is not yet fully ready when Django tries to connect and apply migrations.

To fix it:
```bash
docker-compose down
docker-compose up -d
````

## 🌐 Access
Once running, access the API at:
http://localhost:8080

## 📚 Available Routes

| Path             | Description                |
|------------------|----------------------------|
| `/admin/`        | Django Admin               |
| `/api/v1/`       | API endpoints              |
| `/schema/`       | OpenAPI schema     |
| `/docs/swagger/` | Swagger UI documentation   |
| `/docs/redoc/`   | ReDoc UI documentation     |
