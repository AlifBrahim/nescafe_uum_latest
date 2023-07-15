# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 23:32:14 2023

@author: IMAN ZULHAKIM
"""
from datetime import datetime
from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
# MySQL database configuration
db_config = {
    'host': 'cctmcagenda2.mysql.database.azure.com',
    'port': 3306,
    'user': 'alif',
    'password': 'alep1234!',
    'database': 'spa'
}

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        # Get form inputs
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        event_name = request.form['event_name']
        location = request.form['location']
        coffee = request.form.getlist('coffee[]')
        quantity = request.form.getlist('quantity[]')
        # Format the appointment_date value to YYYY-MM-DD
        appointment_date = datetime.strptime(request.form['appointment_date'], '%m/%d/%Y').strftime('%Y-%m-%d')
        # Format the appointment_time value to HH:MM:SS
        appointment_time = datetime.strptime(request.form['appointment_time'], '%I:%M%p').strftime('%H:%M:%S')
        phone = request.form['phone']
        message = request.form['message']

        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert the data into the nescafe table
        query = "   INSERT INTO nescafe (first_name, last_name, event_name, location, coffee, quantity, appointment_date, appointment_time, phone, message) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, event_name, location, ', '.join(coffee), ', '.join(quantity), appointment_date,
                  appointment_time, phone, message)
        cursor.execute(query, values)

        # Commit the changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()

        return 'Data added to the database successfully!'
    return render_template('menu.html')


@app.route('/services')
def service():
    return render_template('services.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cart')
def cart():
    # Get the cart from the session
    cart = session.get('cart', [])
    # Pass the cart to the template
    return render_template('cart.html', cart=cart)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    payment_method = request.form.get('payment_method')
    print('payment_method:', payment_method)
    # Get the cart from the session
    cart = session.get('cart', [])
    # Calculate the subtotal and total
    subtotal = sum(item['price'] * item['quantity'] for item in cart)
    delivery = 0.00  # Set delivery fee here
    total = subtotal + delivery

    if request.method == 'POST':
        print(request.form)
        # Get the form data
        first_name = request.form.get('first_name')
        location = request.form.get('location')
        phone = request.form.get('phone')
        email_address = request.form.get('email_address')
        pickup_delivery = request.form.get('pickup_delivery')
        payment_method = request.form.get('payment_method')
        terms_conditions = request.form.get('terms_conditions', 0)

        # Calculate the subtotal, delivery, and total
        subtotal = float(request.form.get('subtotal'))
        delivery = float(request.form.get('delivery'))
        total = subtotal + delivery

        # Create a connection to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert the form data into the database
        query = """
            INSERT INTO orders (
                first_name, location, phone, email_address, pickup_delivery,
                subtotal, total, payment_method, terms_conditions, delivery
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (first_name, location, phone, email_address,
                               pickup_delivery, subtotal, total, payment_method,
                               terms_conditions, delivery))

        # Commit the transaction and close the connection
        conn.commit()
        cursor.close()
        conn.close()

    # Pass the cart and calculated values to the template
    return render_template(
        'checkout.html',
        cart=cart,
    )




@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/product')
def product():
    return render_template('product-single.html')



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)