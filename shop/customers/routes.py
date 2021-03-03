from flask import render_template,session, redirect,url_for,flash, make_response
from flask_login import login_required, current_user, logout_user, login_user
from shop import app,db, bcrypt
from .forms import CustomerRegisterForm, CustomerLoginFrom, RatingForm
# from .forms import  RatingForm
from .model import Register, CustomerOrder, Rating
from shop.products.models import Addproduct, SoldProducts
from flask_login import current_user as buyer
# from .model import Rating
from shop import start_timer, stop_timer
import random
import secrets
import pdfkit
import stripe
import zeep
import time
import grpc
# from json import jsonify
from shop.grpc_server.onlineshopping_pb2 import AccountCreationRequest, AccountLoginRequest
from shop.grpc_server.onlineshopping_pb2_grpc import BuyerActionsStub

from flask import request
from shop import grpc_client

buplishable_key ='pk_test_51IN5nDCVZ5Yf06wRG9BLSKuBUaUqXKWKxbQPjAtHcsYdZgY0NiTG0aXIf25Ll29ItyhvnxjBa1FSUJPCo107MmCD00nkqBkcID'
stripe.api_key ='sk_test_51IN5nDCVZ5Yf06wROWN3sRW7aVEhhCfo3obH4jNrU1MuzrOVeLS03hIwbs3UHOcL0v356Z01J1eP8rpcOZT6tQjF00HLVt218C'

@app.route('/payment',methods=['POST'])
def payment():
    invoice = request.form.get('invoice')
    amount = request.form.get('amount')
    customer = stripe.Customer.create(
      email=request.form['stripeEmail'],
      source=request.form['stripeToken'],
    )
    # charge = stripe.Charge.create(
    #   customer=customer.id,
    #   description='Myshop',
    #   amount=amount,
    #   currency='usd',
    # )
        
    orders =  CustomerOrder.query.filter_by(customer_id = current_user.id,invoice=invoice).order_by(CustomerOrder.id.desc()).first()
    orders.status = 'Paid'
    db.session.commit()
    result = makeTransaction(order=invoice)
    if result:
        for key, prod in orders.orders.items():
            product = Addproduct.query.get_or_404(key)
            product.stock = product.stock - prod['quantity']
            db.session.commit()
            soldproducts= SoldProducts.query.filter_by(product=product.name).first()
            soldproducts.update_stock(sellername=soldproducts.name, prod=product.name, quantity_sold=prod['quantity'])
            # prods[seller.name]= product.name
            db.session.commit()
    return redirect(url_for('thanks'))


def makeTransaction(order):
    transport = zeep.Transport(cache=None)
    client = zeep.Client("https://soap-server-vlhiisghja-uc.a.run.app?WSDL", transport=transport)
    st = time.time()
    result = client.service.slow_request()  # takes 1 sec
    print("Time: %.2f" % (time.time() - st))
    return result

@app.route('/thanks')
def thanks():
    return render_template('customer/thank.html')

@app.route('/rating/<seller>/<product>', methods=['GET','POST'])
def rating(seller, product):
    form= RatingForm()
    if form.validate_on_submit():
        id = random.randint(0, 10000)
        rating= Rating(id=id, product=product, rating=form.rating.data, sellername=seller)
        db.session.add(rating)
        flash(f'Thank you for submitting your rating', 'success')
        db.session.commit()
        return redirect(url_for('displayOrders'))
    return render_template('customer/rating.html', form=form, product=product, seller=seller)

@app.route('/customer/register', methods=['GET','POST'])
def customer_register():
    form = CustomerRegisterForm()
    if form.validate_on_submit():
        resp_time = start_timer()
        input_request = AccountCreationRequest \
            (buyer_id=random.randint(0, 10000),
             buyer_name=form.name.data,
             buyer_email=form.email.data,
             buyer_username=form.username.data,
             buyer_password=form.password.data,
             items_purchased = 0,
             buyer_city=form.city.data,
             buyer_contact=form.contact.data,
             buyer_address=form.address.data,
             buyer_country=form.country.data,
             buyer_zipcode=form.zipcode.data,
             )
        # register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, city=form.city.data,contact=form.contact.data, address=form.address.data, zipcode=form.zipcode.data)
        response = grpc_client.createAccount(input_request)
        # db.session.add(register)
        stop_timer(resp_time, "buyerCreateAccount")
        if(response.status == "success"):
            flash(f'Welcome {form.name.data} Thank you for registering! Login now', 'success')
            return redirect(url_for('customerLogin'))

        # db.session.commit()
        else:
            flash(f'Error in registering for {form.name.data}. Try again', 'danger')
            return redirect(url_for('customerRegister'))
    return render_template('customer/register.html', form=form)


@app.route('/customer/login', methods=['GET','POST'])
def customerLogin():
    resp_time= start_timer()
    form = CustomerLoginFrom()
    try:
        if form.validate_on_submit():
            resp_time = start_timer()
            input_request = AccountLoginRequest(buyer_username=form.email.data, buyer_password=form.password.data)
            # user = Register.query.filter_by(email=form.email.data).first()
            user = grpc_client.login(input_request)
            newUser = Register(id=user.buyer_id, name=user.buyer_name, username=user.buyer_username,
                                email=user.buyer_email, password=user.buyer_password, country=user.buyer_country,
                                city=user.buyer_city, contact=user.buyer_contact, address=user.buyer_address,
                                zipcode=user.buyer_zipcode, itemspurchased=user.items_purchased)
            stop_timer(resp_time, "buyer_login")
            if user.is_active == "true":
                login_user(newUser)
                flash('You are login now!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Incorrect email and password', 'danger')
                return redirect(url_for('customerLogin'))
    except Exception as e:
        print(e)
    return render_template('customer/login.html', form=form)


@app.route('/customer/logout')
def customer_logout():
    logout_user()
    return redirect(url_for('home'))

def updateshoppingcart():
    for key, shopping in session['Shoppingcart'].items():
        session.modified = True
        del shopping['image']
        del shopping['colors']
    return updateshoppingcart

@app.route('/getorder')
@login_required
def get_order():
    if current_user.is_authenticated:
        customer_id = current_user.id
        invoice = secrets.token_hex(5)
        id = random.randint(0, 100000)
        updateshoppingcart
        try:
            order = CustomerOrder(id=id, invoice=invoice,customer_id=customer_id,orders=session['Shoppingcart'])
            db.session.add(order)
            db.session.commit()
            session.pop('Shoppingcart')
            flash('Your order has been sent successfully','success')
            return redirect(url_for('orders',invoice=invoice))
        except Exception as e:
            print(e)
            flash('Some thing went wrong while get order', 'danger')
            return redirect(url_for('getCart'))
        


@app.route('/orders/<invoice>')
@login_required
def orders(invoice):
    if current_user.is_authenticated:
        grandTotal = 0
        subTotal = 0
        customer_id = current_user.id
        customer = Register.query.filter_by(id=customer_id).first()
        orders = CustomerOrder.query.filter_by(customer_id=customer_id, invoice=invoice).order_by(CustomerOrder.id.desc()).first()
        for _key, product in orders.orders.items():
            discount = (product['discount']/100) * float(product['price'])
            subTotal += float(product['price']) * int(product['quantity'])
            subTotal -= discount
            tax = ("%.2f" % (.06 * float(subTotal)))
            grandTotal = ("%.2f" % (1.06 * float(subTotal)))

    else:
        return redirect(url_for('customerLogin'))
    return render_template('customer/order.html', invoice=invoice, tax=tax,subTotal=subTotal,grandTotal=grandTotal,customer=customer,orders=orders)

@app.route('/displayorders')
@login_required
def displayOrders():
    if current_user.is_authenticated:
        sellers = []
        grandTotal = 0
        subTotal = 0
        customer_id = current_user.id
        customer = Register.query.filter_by(id=customer_id).first()
        orders = CustomerOrder.query.filter_by(customer_id=customer_id).order_by(CustomerOrder.id.desc()).first()
        for _key, product in orders.orders.items():
            soldproducts= SoldProducts.query.filter_by(product=product['name']).first()
            sellers.append(soldproducts.name)
            discount = (product['discount']/100) * float(product['price'])
            subTotal += float(product['price']) * int(product['quantity'])
            subTotal -= discount
            tax = ("%.2f" % (.06 * float(subTotal)))
            grandTotal = ("%.2f" % (1.06 * float(subTotal)))

    else:
        return redirect(url_for('customerLogin'))
    return render_template('customer/displayOrders.html', tax=tax,subTotal=subTotal,grandTotal=grandTotal,customer=customer,orders=orders, sellers=sellers)


@app.route('/get_pdf/<invoice>', methods=['POST'])
@login_required
def get_pdf(invoice):
    if current_user.is_authenticated:
        grandTotal = 0
        subTotal = 0
        customer_id = current_user.id
        if request.method =="POST":
            customer = Register.query.filter_by(id=customer_id).first()
            orders = CustomerOrder.query.filter_by(customer_id=customer_id, invoice=invoice).order_by(CustomerOrder.id.desc()).first()
            for _key, product in orders.orders.items():
                discount = (product['discount']/100) * float(product['price'])
                subTotal += float(product['price']) * int(product['quantity'])
                subTotal -= discount
                tax = ("%.2f" % (.06 * float(subTotal)))
                grandTotal = float("%.2f" % (1.06 * subTotal))

            rendered =  render_template('customer/pdf.html', invoice=invoice, tax=tax,grandTotal=grandTotal,customer=customer,orders=orders)
            pdf = pdfkit.from_string(rendered, False)
            response = make_response(pdf)
            response.headers['content-Type'] ='application/pdf'
            response.headers['content-Disposition'] ='inline; filename='+invoice+'.pdf'
            return response
    return request(url_for('orders'))



