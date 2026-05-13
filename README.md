# Product Catalog API

This Flask application creates a simple RESTful GET API for a fictional product catalog.

## Features

- `GET /` returns a welcome message.
- `GET /products` returns all products.
- `GET /products/<id>` returns one product by ID.
- `GET /products?category=books` filters products by category.
- Returns a `404` response when a product is not found.

## How to Run

```bash
python --version
pip install flask
python app.py