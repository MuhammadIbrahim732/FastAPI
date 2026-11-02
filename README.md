# FastAPI E-Commerce Product API

A RESTful Product Management API built with **FastAPI and Pydantic**. This project demonstrates CRUD operations, request validation, product searching, price sorting, UUID-based identification, and timestamp generation.

## 🚀 Features

### 1. CRUD Operations

Implemented the four main product management operations:

- **GET** – Retrieve all products.
- **POST** – Add a new product.
- **PUT** – Update an existing product.
- **DELETE** – Remove a product.

### 2. Product Search

- Search products by name.
- Case-insensitive search.
- Handles cases where no matching product is found.
- Query parameter validation using FastAPI's `Query`.

### 3. Product Sorting

- Sort products by price.
- Support for ascending (`asc`) and descending (`desc`) order.
- Optional sorting through query parameters.

### 4. Data Validation

Used Pydantic schemas:

- `Product` for creating products.
- `ProductUpdate` for updating products.
- Validated request data before processing.

### 5. UUID Generation

- Automatically generates a unique UUID for every new product.
- Uses UUID path parameters for product updates and deletion.

### 6. Timestamp Generation

Automatically generates a UTC timestamp when a product is created using Python's `datetime` module.

### 7. Error Handling

Implemented HTTP exception handling for different scenarios:

| Status Code | Description |
|---|---|
| 201 | Product created successfully |
| 400 | Invalid product creation request |
| 404 | Product not found |

## 🛠️ Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- UUID
- Python Datetime

## 📁 Project Structure

```text
fastapi-ecommerce/
│
├── app/
│   ├── data/
│   │   └── products.json
│   │
│   ├── schema/
│   │   └── product.py
│   │
│   ├── services/
│   │   └── products.py
│   │
│   └── main.py
│
└── requirements.txt
```

*Note: This is an example structure based on the modules imported in the application. Adjust it to match your actual repository.*

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/products` | Retrieve products |
| POST | `/products` | Create a product |
| PUT | `/products/{product_id}` | Update a product |
| DELETE | `/products/{product_id}` | Delete a product |

### GET – Search and Sort Products

Example:

```http
GET /products?name=xiaomi
```

Sort products by price:

```http
GET /products?sort_by_price=true&order=asc
```

Sort in descending order:

```http
GET /products?sort_by_price=true&order=desc
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd fastapi-ecommerce
```

**3. Create a virtual environment**

```bash
python -m venv .venv
```

**4. Activate the environment**

Windows:

```bash
.venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install fastapi uvicorn pydantic
```

**6. Run the application**

```bash
uvicorn app.main:app --reload
```

## 📚 API Documentation

Once the application is running, access the interactive API documentation:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 🎯 Learning Outcomes

Through this project, I practiced:

- Building REST APIs with FastAPI.
- Implementing CRUD operations.
- Working with HTTP methods and status codes.
- Using path and query parameters.
- Validating request data with Pydantic.
- Generating UUIDs and timestamps.
- Implementing search and sorting functionality.
- Organizing application logic into schemas, services, and API routes.
- Handling errors using HTTPException.

## 👨‍💻 Author

**Muhammad Ibrahim**

AI/ML Engineering Learner | Python | Machine Learning | Deep Learning | Generative AI

- GitHub: https://github.com/MuhammadIbrahim732
- LinkedIn: https://www.linkedin.com/in/muhammad-ibrahim-4a8425330/

---

⭐ If you find this project useful, consider giving it a star!
