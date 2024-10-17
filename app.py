from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

# Global variables to store cart items and total
cart = []
total_amount = 0

# Route for home page
@app.route('/')
def home():
    return render_template('index.html', cart=cart, total_amount=total_amount)

# API to add item to cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    global total_amount

    item_name = request.form['item_name']
    item_price = float(request.form['item_price'])
    item_quantity = int(request.form['item_quantity'])

    if item_name and item_price > 0 and item_quantity > 0:
        total_item_price = item_price * item_quantity
        total_amount += total_item_price
        cart.append({
            'name': item_name,
            'quantity': item_quantity,
            'price': total_item_price
        })
        return redirect(url_for('home'))
    return "Invalid input", 400

# API to reset the cart
@app.route('/reset', methods=['POST'])
def reset():
    global cart, total_amount
    cart.clear()
    total_amount = 0
    return redirect(url_for('home'))

# API to generate receipt and download as text file
@app.route('/checkout', methods=['POST'])
def checkout():
    if total_amount == 0:
        return "No items in cart", 400
    
    receipt = "Mall Cashier Receipt\n"
    receipt += "===========================\n"
    for item in cart:
        receipt += f"{item['name']} x{item['quantity']} \tRp {item['price']}\n"
    receipt += f"===========================\nTotal: Rp {total_amount}\n"
    receipt += "Thank you for shopping!\n"

    with open('receipt.txt', 'w') as f:
        f.write(receipt)

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
