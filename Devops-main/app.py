from urllib.parse import quote_plus
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env
load_dotenv()

USERNAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')


# URL-encode the username and password
encoded_username = quote_plus(USERNAME)
encoded_password = quote_plus(PASSWORD)

# Connect to MongoDB Atlas
client = MongoClient(f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.onhos.mongodb.net/shop_db?retryWrites=true&w=majority")

# Access the `shop_db` database and `products` collection
db = client.shop_db
products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    # Convert cursor to a list to avoid errors
    products = list(products_collection.find())
    
    # Print debug information
    print(f"Total products found: {len(products)}")
    for product in products:
        print(product)
    
    # Pass the products to the template
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
