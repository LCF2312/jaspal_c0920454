from urllib.parse import quote_plus
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

username = "c0920454"  # replace with your actual username
password = "vjding5y10fY8WXN"  # replace with your actual password

# # URL-encode the username and password
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# Connect to MongoDB Atlas
client = MongoClient(f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.onhos.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.shop_db
products_collection = db.products

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()
    # print("After Products="+str(len(products)))
    # for i in products:
    #     print(i)
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)



