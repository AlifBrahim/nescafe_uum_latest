# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 23:32:14 2023

@author: IMAN ZULHAKIM
"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
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


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)
