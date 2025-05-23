# 🛒 Fast Seller API

A modern, fast, and scalable RESTful API built with **FastAPI**, **Uvicorn**, **SQLAlchemy**, **Pydantic**, and **PostgreSQL**.  
Designed to power a commercial platform with secure authentication, customer and product management, and a complete order system.

---

## 🚀 Features

- ✅ **JWT Authentication**
- 👤 **Client Management**
- 📦 **Product Inventory**
- 🧾 **Order Processing**
- 📄 Built with **FastAPI**, using async support
- 🛢️ Uses **PostgreSQL** with **SQLAlchemy ORM**
- 📐 Data validation with **Pydantic**

---

## 📌 Endpoints Overview

### 🔐 Authentication

| Method | Endpoint              | Description                   |
|--------|------------------------|-------------------------------|
| POST   | `/auth/login`         | Authenticate user and return token |
| POST   | `/auth/register`      | Register a new user           |
| POST   | `/auth/refresh-token` | Refresh JWT token             |

---

### 👥 Clients

| Method | Endpoint         | Description                                       |
|--------|------------------|---------------------------------------------------|
| GET    | `/clients`       | List all clients (with pagination and filters by name and email) |
| POST   | `/clients`       | Create a new client (unique email and CPF)        |
| GET    | `/clients/{id}`  | Retrieve a specific client                       |
| PUT    | `/clients/{id}`  | Update a specific client                         |
| DELETE | `/clients/{id}`  | Delete a client                                  |

---

### 🛍️ Products

| Method | Endpoint           | Description                                          |
|--------|--------------------|------------------------------------------------------|
| GET    | `/products`        | List all products (with pagination and filters)      |
| POST   | `/products`        | Create a new product (with images and validation)    |
| GET    | `/products/{id}`   | Retrieve a specific product                         |
| PUT    | `/products/{id}`   | Update a specific product                           |
| DELETE | `/products/{id}`   | Delete a product                                    |

---

### 📦 Orders

| Method | Endpoint         | Description                                                                |
|--------|------------------|----------------------------------------------------------------------------|
| GET    | `/orders`        | List all orders (filter by date, section, order ID, status, client)       |
| POST   | `/orders`        | Create a new order with multiple products (stock validation)              |
| GET    | `/orders/{id}`   | Retrieve a specific order                                                 |
| PUT    | `/orders/{id}`   | Update a specific order (including status)                                |
| DELETE | `/orders/{id}`   | Delete an order                                                           |

---

## 🧰 Tech Stack

- **FastAPI** - web framework
- **Uvicorn** - ASGI server
- **SQLAlchemy** - ORM for database interaction
- **Pydantic** - data validation and serialization
- **PostgreSQL** - relational database

---

## 🚧 Installation

### Clone the repository
```
```
git clone https://github.com/your-user/fast-seller-api.git
cd fast-seller-api
```
```

### Create virtual environment
``` 
```
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
``` 
```

### Install dependencies
``` 
```
pip install -r requirements.txt
```
```

### Run the server
```
```
python app/main.python 
```


```
##📋 License

MIT-3 © 2025 jean0t  

## Contributions

Contributors are welcome, may it be forks or pull requests!  
