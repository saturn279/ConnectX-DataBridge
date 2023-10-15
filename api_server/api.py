from flask import Flask, jsonify
import random
import faker
import json

app = Flask(__name__)
fake = faker.Faker()

# Function to generate random product data for a category
def generate_product_data(category):
    product_name = fake.catch_phrase()
    price = round(random.uniform(10, 500), 2)
    quantity = random.randint(1, 100)
    product_data = {
        "category": category,
        "product_name": product_name,
        "price": price,
        "quantity": quantity
    }
    return product_data

# Endpoint to get product data
@app.route('/api/products', methods=['GET'])
def get_products():
    categories = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Toys", "Beauty"]
    product_data = [generate_product_data(category) for category in categories]
    return jsonify(product_data)

if __name__ == '__main__':
    # Run the Flask app on http://localhost:5000/api/products
    app.run(host='0.0.0.0', port=80, debug=True)
