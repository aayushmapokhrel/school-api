# 📘 School Management System API

Hey there! 👋\
Welcome to the **School Management System API** — a Django-powered RESTful API built to help you manage schools, students, and teachers effortlessly. Whether you're building a school portal backend or just exploring Django magic, this project has your back.

---

## 🚀 Getting Started

Here’s a quick guide to get this project up and running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/aayushmapokhrel/school-api.git
cd school-api
```

### 2. Set Up a Virtual Environment

We recommend using a virtual environment for package management:

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
# OR
venv\Scripts\activate       # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> 💡 Ensure you have `pip` installed and updated!

---

## 🛠️ MySQL Database Setup

Make sure MySQL is installed and running.

1. Log in to MySQL:

```sql
CREATE DATABASE school_api_db;
```

2. Create a MySQL user (if you haven't already) and grant privileges.

---

### 4. Add Environment Variables

Create a `.env` file in your project root and add:

```
DB_NAME=school_api_db
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

---

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Start the Development Server 🔥

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 🔑 JWT Authentication (Superuser Access)

This project uses JWT (JSON Web Tokens) for authentication.

### Step 1: Create a Superuser

To access protected endpoints, create a superuser:

```bash
python manage.py createsuperuser
```

Provide your desired `username`, `email`, and `password`.

---

### Step 2: Obtain Access and Refresh Tokens

Use this endpoint to get your tokens:

```http
POST /api/token/
Content-Type: application/json

{
  "username": "your_superuser_username",
  "password": "your_superuser_password"
}
```

Response:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

---

### Step 3: Authenticate Your Requests

Add this header to all secured requests:

```http
Authorization: Bearer your_access_token
```

---

### Step 4: Refresh Expired Tokens

```http
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "your_refresh_token"
}
```

---

## 🔌 Example API Requests

### Create a School

```http
POST /api/schools/
Content-Type: application/json

{
  "name": "ABC School",
  "address": "New York"
}
```

### Create a Student

```http
GET /api/students/
```Content-Type: application/json
{
  "name": "student_name",
  "age": "student_age",
  "grade": 5
  "school":1
}
```

### Create a Teacher

```http
POST /api/teachers/
Content-Type: application/json

{
  "name": "Aayushma Pokhrel",
  "subject": "Mathematics",
  "school": 1
}
```

---

## 🔌 API Endpoints (CRUD Operations)

### Schools

| Method | Endpoint            | Description            |
|--------|---------------------|------------------------|
| GET    | /api/schools/       | List all schools       |
| POST   | /api/schools/       | Create a new school    |
| GET    | /api/schools/{id}/  | Retrieve school by ID  |
| PUT    | /api/schools/{id}/  | Update school by ID    |
| DELETE | /api/schools/{id}/  | Delete school by ID    |

---

### Students

| Method | Endpoint             | Description              |
|--------|----------------------|--------------------------|
| GET    | /api/students/       | List all students        |
| POST   | /api/students/       | Create a new student     |
| GET    | /api/students/{id}/  | Retrieve student by ID   |
| PUT    | /api/students/{id}/  | Update student by ID     |
| DELETE | /api/students/{id}/  | Delete student by ID     |

---

### Teachers

| Method | Endpoint             | Description              |
|--------|----------------------|--------------------------|
| GET    | /api/teachers/       | List all teachers        |
| POST   | /api/teachers/       | Create a new teacher     |
| GET    | /api/teachers/{id}/  | Retrieve teacher by ID   |
| PUT    | /api/teachers/{id}/  | Update teacher by ID     |
| DELETE | /api/teachers/{id}/  | Delete teacher by ID     |

---

## 💃 Contributing

Feel free to fork this repo, improve it, or raise an issue. Any contributions are super welcome! 🎉

---

