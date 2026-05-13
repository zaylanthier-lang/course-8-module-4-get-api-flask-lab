from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# Homepage route that returns a welcome message

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Product Catalog API"}), 200


# GET /products route that returns all products or filters by category

@app.route("/products")
def get_products():
    category = request.args.get("category")

    if category:
        filtered_products = [
            product for product in products
            if product["category"] == category
        ]
        return jsonify(filtered_products), 200

    return jsonify(products), 200


# GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>")
def get_product_by_id(id):

    for product in products:
        if product["id"] == id:
            return jsonify(product), 200

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)