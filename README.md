# DRF APIs

This repository some Django REST Framework (DRF) applications:

1. **Task Management API**: Provides basic CRUD operations, pagination, and authentication.
2. **Blog API**: Implements basic CRUD operations, pagination, authentication, and a comments system.

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/rohitatzignuts/drf-api.git
```

### 2. Set up a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

### 3. Install the dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser for the Django admin:

```bash
python manage.py createsuperuser
```

### 6. Run the server:

```bash
python manage.py runserver
```

---

## Task Management API

This app allows users to manage tasks by performing Create, Read, Update, and Delete (CRUD) operations. Authentication is required for certain actions.

### Key Features:

- **CRUD operations**: Create, retrieve, update, and delete tasks.
- **Pagination**: Paginated lists of tasks for easier management.
- **Authentication**: Secure API using Django's authentication system.

## Blog API

The Blog API enables basic blog post management and comments system. Users can create blog posts, comment on them, and view them with pagination.

### Key Features:

- **CRUD operations**: Create, retrieve, update, and delete blog posts.
- **Comments**: Allows users to add comments to blog posts.
- **Pagination**: Paginated lists of blog posts.
- **Authentication**: Required for creating and editing blog posts.

## Authentication

Both applications use token-based authentication. Users must be authenticated to perform certain actions like creating, updating, or deleting tasks or blogs.

To authenticate:

- Obtain a token via login.
- Include the token in the `Authorization` header of your requests as follows:

```bash
Authorization: Token your_token
```

---

## Pagination

Pagination is enabled by default in both the Task Management and Blog APIs. Requests to list tasks or blogs will return paginated results.

---
