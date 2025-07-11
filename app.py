from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 101, "name": "Laptop", "price": 1200},
    {"id": 102, "name": "Mouse", "price": 25}
]

@app.route('/')
def home():
    return "Product Service is running!"

@app.route('/products')
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>')
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
