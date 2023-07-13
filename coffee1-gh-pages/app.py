# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 23:32:14 2023

@author: IMAN ZULHAKIM
"""
from datetime import datetime
from flask import Flask, render_template, request
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
        query = "INSERT INTO nescafe (first_name, last_name, event_name, location, coffee, quantity, appointment_date, appointment_time, phone, message) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, event_name, location, ', '.join(coffee), ', '.join(quantity), appointment_date, appointment_time, phone, message)
        cursor.execute(query, values)

        # Commit the changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()

        return 'Data added to the database successfully!'

    return render_template('index.html')



@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/services')
def service():
    return render_template('services.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

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
