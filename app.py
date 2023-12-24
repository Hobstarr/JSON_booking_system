from flask import Flask, render_template, request
import datetime
import random

from main import Customer, new_customer, print_all_customers, load_customer, get_all_customers


app = Flask(__name__)


from faker import Faker
fake = Faker()






@app.route('/')
def hello():
    return render_template('index.html',                       
            utc_dt = datetime.datetime.utcnow().date(),
            name = fake.name())

@app.route('/newcustomer/', methods=["GET", "POST"])
def new_cust():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        return render_template('newcustomer_success.html', 
                               name = name, age = age)
    else:
        return render_template('newcustomer.html')
    
@app.route('/show_all_customers/')
def all_customers():
    customers = get_all_customers()
    return render_template('show_all_customers.html', customers=customers)
    
@app.route('/customers/<user_id>/')
def customers(user_id):
    customer_loaded = load_customer(user_id)
    return render_template('customer.html', customer = customer_loaded)
    

@app.route('/comments/')
def comments():
    customers = get_all_customers()
    return render_template('comments.html', customers=customers)