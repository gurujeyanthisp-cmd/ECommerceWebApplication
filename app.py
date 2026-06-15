from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mobile", "price": 20000},
    {"name": "Headphones", "price": 2000}
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)