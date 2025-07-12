# 📚 FastAPI Bookstore API

RESTful API for managing a bookstore, built with **FastAPI**, **MongoDB**, and **Pydantic**. Supports full CRUD operations.

---

## 🚀 Features

- ✅ Create, Read, Update, Delete (CRUD) books
- ✅ MongoDB integration with `motor` (async)
- ✅ Pydantic validation
- ✅ Modular, scalable project structure
- ✅ CORS support for frontend integration
- ✅ `.env` support for environment configuration

---

## 📦 Tech Stack

- **FastAPI** – High-performance Python API framework
- **MongoDB** – NoSQL database
- **Motor** – Async MongoDB driver
- **Pydantic** – Data validation and settings
- **Uvicorn** – ASGI server

---

## 📁 Project Structure
    bookstore/
    │
    ├── app/
    │ ├── main.py # App entry point
    │ ├── database.py # MongoDB client
    │ ├── models.py # (optional) Database models
    │ ├── core/
    │ │ └── config.py # .env loader
    │ ├── schemas/
    │ │ └── book.py # Pydantic models
    │ ├── routes/
    │ │ └── books.py # All API routes
    │ └── utils/
    │ └── bson_utils.py # ObjectId converter
    │
    ├── .env # Secrets and DB config
    ├── .gitignore
    ├── requirements.txt
    └── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the Repo

    https://github.com/shubhankarchdas/FastApi.git
    cd bookstore-api


### 2. Create Virtual Environment

    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate


### 3. Install Dependencies

    pip install -r requirements.txt


### 4. Set Up Environment Variables
Create a .env file in the root with:

    MONGO_URI=mongodb://localhost:27000
    DB_NAME=bookstore_db

▶️ Run the App

    uvicorn app.main:app --reload
